from .genre import GenreDAO
from .director import DirectorDAO
from .movie import MovieDAO
from .users import UserDAO
from .favourite_movies import FavouriteMovieDAO

__all__ = [
    'GenreDAO',
    'DirectorDAO',
    'MovieDAO',
    'UserDAO',
    'FavouriteMovieDAO'
]
