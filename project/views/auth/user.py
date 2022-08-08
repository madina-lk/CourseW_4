
from flask_restx import Resource, Namespace
from flask import request

from project.setup.api.models import user
from project.dao.model.users import UserSchema
from project.container import user_service

from project.tools.security import auth_required, admin_required, check_token

api = Namespace('user')


@api.route('/')
class UsersView(Resource):
    # @auth_required
    @api.marshal_with(user, as_list=True, code=200, description='OK')
    def get(self):
        token = request.headers['Authorization'].split('Bearer')[-1]
        uid = check_token(token)['id']
        return user_service.get_by_uid(uid), 200

    def patch(self):
        token = request.headers['Authorization'].split('Bearer')[-1]
        uid = check_token(token)['id']
        data = request.get_json()
        user_service.update_favourite(data, uid)
        return '', 200


@api.route('/password/')
class UsersView(Resource):
    def put(self):
        token = request.headers['Authorization'].split('Bearer')[-1]
        uid = check_token(token)['id']
        data = request.get_json()
        user_service.update(data, uid)
        return '', 200

