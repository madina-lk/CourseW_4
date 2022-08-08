
from project.dao.base import BaseDAO
from project.dao.model.favourite_movies import FavouriteMovie
from flask_sqlalchemy import BaseQuery
from project.dao.model.movie import Movie


class FavouriteMovieDAO(BaseDAO[FavouriteMovie]):
    __model__ = FavouriteMovie

    def get_favourite_movies(self, uid, mid):
        stmt: BaseQuery = self._db_session.query(self.__model__)
        return stmt.filter(self.__model__.user_id == uid, self.__model__.movie_id == mid).first()

    def get_all(self):
        stmt: BaseQuery = self._db_session.query(self.__model__)
        return stmt.join(Movie).all()

    def create(self, favourite_d):
        try:
            movie = self.__model__(**favourite_d)
            self._db_session.add(movie)
            self._db_session.commit()
            return movie
        except Exception:
            return 'Ошибка'

    def delete(self, uid):
        user = self.__model__(uid)
        self.session.delete(user)
        self.session.commit()
