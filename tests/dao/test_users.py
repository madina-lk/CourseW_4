import pytest

from project.dao import UserDAO
from project.dao.model.users import User


class TestUserDAO:

    @pytest.fixture
    def user_dao(self, db):
        return UserDAO(db.session)

    @pytest.fixture
    def user_1(self, db):
        g = User(
            email="amina67@yahoo.com",
            password='MLIU3S9faPvHb1VEyaNfNM6guVoghg0gS6UyDTspVDs='
        )
        db.session.add(g)
        db.session.commit()
        return g

    @pytest.fixture
    def user_2(self, db):
        g = User(
            email="fightes@mail.ru",
            password='NscPscGKpYIZnk8p7wWhEfPbgc0uFUTuzFPYtRjmzFk='

        )
        db.session.add(g)
        db.session.commit()
        return g

    def test_get_user_by_id(self, user_1, user_dao):
        assert user_dao.get_by_id(user_1.id) == user_1

    def test_get_user_by_id_not_found(self, user_dao):
        assert not user_dao.get_by_id(1)

    def test_get_all_users(self, user_dao, user_1, user_2):
        assert user_dao.get_all() == [user_1, user_2]

    def test_get_user_by_email(self, user_1, user_dao):
        assert user_dao.get_by_email(user_1.email) == user_1


