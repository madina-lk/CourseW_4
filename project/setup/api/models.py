from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

director: Model = api.model('Режиссер', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Режиссер'),
})

movie: Model = api.model('Фильм', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=100, example='Название'),
    'description': fields.String(required=True, max_length=100, example='Описание'),
    'trailer': fields.String(required=True, max_length=100, example='Трейлер'),
    'year': fields.Integer(required=True, max_length=100, example='Год'),
    'rating': fields.Float(required=True, max_length=100, example='Рейтинг'),
    'genre': fields.Nested(genre),
    'director': fields.Nested(director),

})

user: Model = api.model('Пользователь', {
    'id': fields.Integer(required=True, example=1),
    'email': fields.String(required=True, max_length=100, example='Почта'),
    'password': fields.String(required=True, max_length=100, example='Пароль'),
    'name': fields.String(required=True, max_length=100, example='Имя'),
    'surname': fields.String(required=True, max_length=100, example='Фамилия'),
    'favourite_genre': fields.String(required=True, max_length=100, example='Избранное')
})

favourite_movie: Model = api.model('Избранное', {
    'user_id': fields.Integer(required=True, example=1),
    'movie_id': fields.String(required=True, example=2),
    'user': fields.String(required=True, max_length=100, example='Пользователь'),
    'movie': fields.String(required=True, max_length=100, example='Фмльм')
})