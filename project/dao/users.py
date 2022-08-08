
from project.dao.model.users import User

from project.dao.base import BaseDAO
from flask_sqlalchemy import BaseQuery

from typing import Generic, List, Optional, TypeVar


class UserDAO(BaseDAO[User]):
    __model__ = User

    def get_by_email(self, email: Optional[str]):
        stmt: BaseQuery = self._db_session.query(self.__model__)
        return stmt.filter(self.__model__.email == email).first()

    def create(self, **kwargs):
        try:
            self._db_session.add(self.__model__(**kwargs))
            self._db_session.commit()
            return 'Пользователь создан'
        except Exception:
            return 'Пользователь Не создан'

    def update(self, **kwargs):
        self._db_session.add(**kwargs)
        self._db_session.commit()
