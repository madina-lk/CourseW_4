from project.dao.genre import GenreDAO
from project.dao.director import DirectorDAO
from project.dao.movie import MovieDAO
from project.dao.users import UserDAO
from project.dao.favourite_movies import FavouriteMovieDAO

from project.services import GenreService, DirectorService, MovieService, UserService, AuthService, FavouriteMovieService

from project.setup.db import db

# DAO
genre_dao = GenreDAO(db.session)
director_dao = DirectorDAO(db.session)
movie_dao = MovieDAO(db.session)
user_dao = UserDAO(db.session)
favourite_movie_dao = FavouriteMovieDAO

# Services
genre_service = GenreService(dao=genre_dao)
director_service = DirectorService(dao=director_dao)
movie_service = MovieService(dao=movie_dao)
user_service = UserService(dao=user_dao)
auth_service = AuthService(user_service=user_service)
favourite_movie_service = FavouriteMovieService(dao=favourite_movie_dao)

