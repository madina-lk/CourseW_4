
from project.dao.users import UserDAO
import hashlib
import base64
import hmac
from project.tools.security import generate_password_hash, compare_passwords


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_by_email(self, email):
        return self.dao.get_by_email(email)

    def get_by_uid(self, uid):
        return self.dao.get_by_id(uid)

    def create(self, user_data):
        user_data['password'] = generate_password_hash(user_data['password'])
        return self.dao.create(**user_data)

    def update(self, user_data, token):
        user = self.get_by_uid(token)
        if user:
            if compare_passwords(user):
                new_psswrd = self.generate_password_hash(user_data['password'])
                user.password = new_psswrd
                self.dao.update(user, token)
            else:
                return 'Неверный пароль'

    def update_favourite(self, data, access_tk):
        if user := self.get_by_uid(access_tk):
            if 'name' in data:
                user.name = data['name']
            if 'surname' in data:
                user.surname = data['surname']
            if 'favourite_genre' in data:
                user.favourite_genre = data['favourite_genre']
            self.dao.update(user)