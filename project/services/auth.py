import calendar
import datetime

import jwt
from flask import abort

from project.services.user import UserService

from flask import current_app
from project.tools.security import compare_passwords


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_tokens(self, email, password, is_refresh=False):
        user = self.user_service.get_by_email(email)

        if user is None:
            raise abort(404)

        if not is_refresh:
            if not compare_passwords(user.password, password):
                abort(400)

        data = {
            'email': user.email,
            'id': user.id
        }

        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data['exp'] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, current_app.config['SECRET_KEY'], algorithm=current_app.config['ALGORITHM'])

        day130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data['exp'] = calendar.timegm(day130.timetuple())
        refresh_token = jwt.encode(data, current_app.config['SECRET_KEY'], algorithm=current_app.config['ALGORITHM'])

        return {
            'access_token': access_token,
            'refresh_token': refresh_token
        }

    def approve_refresh_token(self, refresh_token):
        data = jwt.decode(jwt=refresh_token, key=current_app.config['SECRET_KEY'], algorithms=current_app.config['ALGORITHM'])
        email = data.get('email')

        user = self.user_service.get_by_email(email)
        if not user:
            return False

        now = calendar.timegm(datetime.datetime.utcnow().timetuple())
        expired = data['exp']
        if now > expired:
            return False

        return self.generate_tokens(email, user.password, is_refresh=True)


