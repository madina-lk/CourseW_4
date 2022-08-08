
from typing import Optional

from project.dao.base import BaseDAO
from project.exceptions import ItemNotFound
from project.dao.model.favourite_movies import FavouriteMovie
from project.dao import FavouriteMovieDAO

from typing import List


class FavouriteMovieService:
    def __init__(self, dao: FavouriteMovieDAO) -> None:
        self.dao = dao

    def create(self, uid, mid) -> object:
        data = {
            'user_id': uid,
            'movie_id': mid
        }

        if self.dao.get_favourite_movies(uid, mid):
            return 'Фильм уже добавлен'

        return self.dao.create(data)

    def get_favourite_movie(self) -> List[FavouriteMovie]:
        return self.dao.get_all()

    def delete(self, uid, mid):
        favourite_movie = self.dao.get_favourite_movies(uid, mid)
        self.dao.delete(favourite_movie[0].id)

