from marshmallow import Schema, fields
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from project.setup.db import models

from project.dao.model.users import UserSchema
from project.dao.model.movie import MovieSchema


class FavouriteMovie(models.Base):
    __tablename__ = 'favouritemovie'
    user_id = Column(Integer, ForeignKey('user.id'))
    movie_id = Column(Integer, ForeignKey('movie.id'))
    user = relationship("User")
    movie = relationship("Movie")


class FavouriteMovieSchema(Schema):
    user_id = fields.Int()
    movie_id = fields.Int()
    user = fields.Pluck(UserSchema, 'name')
    movie = fields.Pluck(MovieSchema, 'title')

