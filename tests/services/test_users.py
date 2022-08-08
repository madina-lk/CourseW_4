from unittest.mock import patch

import pytest

from project.exceptions import ItemNotFound
from project.dao.model.users import User
from project.services import UserService


class TestUserService:

    @pytest.fixture()
    @patch('project.dao.UserDAO')
    def user_dao_mock(self, dao_mock):
        dao = dao_mock()
        dao.get_by_id.return_value = User(
            email="amina67@yahoo.com",
            password='MLIU3S9faPvHb1VEyaNfNM6guVoghg0gS6UyDTspVDs='
        )
        dao.get_all.return_value = [
            User(
                email="amina67@yahoo.com",
                password='MLIU3S9faPvHb1VEyaNfNM6guVoghg0gS6UyDTspVDs='
            ),
            User(
                email="fightes@mail.ru",
                password='NscPscGKpYIZnk8p7wWhEfPbgc0uFUTuzFPYtRjmzFk='

            ),
        ]
        return dao

    @pytest.fixture()
    def user_service(self, user_dao_mock):
        return UserService(dao=user_dao_mock)

    @pytest.fixture
    def user(self, db):
        obj = User(
            email="fightes@mail.ru",
            password='NscPscGKpYIZnk8p7wWhEfPbgc0uFUTuzFPYtRjmzFk='

        )
        db.session.add(obj)
        db.session.commit()
        return obj

    def test_get_user_by_id(self, user, user_service):
        assert user_service.get_by_uid(user.id) == user

    def test_user_not_found(self, user_dao_mock, user_service):
        user_dao_mock.get_by_id.return_value = None

        with pytest.raises(ItemNotFound):
            user_service.get_by_uid(10)
