
from marshmallow import Schema, fields
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from project.setup.db import models


class User(models.Base):
    __tablename__ = 'user'

    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), unique=True, nullable=False)
    name = Column(String)
    surname = Column(String)
    favourite_genre = Column(Integer(), ForeignKey('genre.id'))
    genre = relationship('Genre')


class UserSchema(Schema):
    email = fields.Str()
    password = fields.Str()
    name = fields.Str()
    surname = fields.Str()
    favourite_genre = fields.Int()

