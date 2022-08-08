
from flask_restx import Resource, Namespace
from flask import request

from project.container import auth_service, user_service

api = Namespace('auth')


@api.route('/register/')
class AuthView(Resource):

    def post(self):
        data = request.json
        user_service.create(data)
        return 'Пользователь создан', 201


@api.route('/login/')
class AuthView(Resource):

    def post(self):
        data = request.json

        email = data.get('email')
        password = data.get('password')

        if None in [email, password]:
            return 'Не введены email, пароль', 400

        tokens = auth_service.generate_tokens(email, password)

        if tokens:
            return tokens, 201
        else:
            return '', 400

    def put(self):
        data = request.json

        token = data.get('refresh_token')
        if not token:
            return 'Токен не задан', 400

        tokens = auth_service.approve_refresh_token(token)
        if tokens:
            return tokens, 200
        else:
            return 'ytd'

