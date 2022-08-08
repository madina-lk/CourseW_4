
from flask_restx import Namespace, Resource
from flask import request

from project.container import favourite_movie_service
from project.dao.model.movie import MovieSchema
from project.tools.security import auth_required, check_token

api = Namespace('favourites')


@auth_required
@api.route('/movies/')
class FavouriteMoviesView(Resource):
    def get(self):
        fav_res = favourite_movie_service.get_favourite_movie()
        result = MovieSchema(many=True).dump(fav_res)
        return result, 200


@auth_required
@api.route('/movies/<int:movie_id>/')
class FavouriteMoviesView(Resource):
    def post(self, movie_id):
        token = request.headers['Authorization'].split('Bearer')[-1]
        access_token = check_token(token)['id']
        favourite_movie_service.create(access_token, movie_id)
        return '', 200

    def delete(self, movie_id):
        token = request.headers['Authorization'].split('Bearer')[-1]
        access_token = check_token(token)['id']
        favourite_movie_service.delete(access_token, movie_id)
        return '', 200
