import pytest

from project.dao import DirectorDAO
from project.dao.model.director import Director


class TestDirectorsDAO:

    @pytest.fixture
    def director_dao(self, db):
        return DirectorDAO(db.session)

    @pytest.fixture
    def director_1(self, db):
        g = Director(name="Тейлор Шеридан")
        db.session.add(g)
        db.session.commit()
        return g

    @pytest.fixture
    def director_2(self, db):
        g = Director(name="Квентин Тарантино")
        db.session.add(g)
        db.session.commit()
        return g

    def test_get_director_by_id(self, director_1, director_dao):
        assert director_dao.get_by_id(director_1.id) == director_1

    def test_get_director_by_id_not_found(self, director_dao):
        assert not director_dao.get_by_id(1)

    def test_get_all_directors(self, director_dao, director_1, director_2):
        assert director_dao.get_all() == [director_1, director_2]

    def test_get_directors_by_page(self, app, director_dao, director_1, director_2):
        app.config['ITEMS_PER_PAGE'] = 1
        assert director_dao.get_all(page=1) == [director_1]
        assert director_dao.get_all(page=2) == [director_2]
        assert director_dao.get_all(page=3) == []
