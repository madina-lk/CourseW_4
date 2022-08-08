from unittest.mock import patch

import pytest

from project.exceptions import ItemNotFound
from project.dao.model.director import Director
from project.services import DirectorService


class TestDirectorService:

    @pytest.fixture()
    @patch('project.dao.DirectorDAO')
    def director_dao_mock(self, dao_mock):
        dao = dao_mock()
        dao.get_by_id.return_value = Director(id=1, name='test_director')
        dao.get_all.return_value = [
            Director(id=1, name='test_director_1'),
            Director(id=2, name='test_director_2'),
        ]
        return dao

    @pytest.fixture()
    def director_service(self, director_dao_mock):
        return DirectorService(dao=director_dao_mock)

    @pytest.fixture
    def director(self, db):
        obj = Director(name="director")
        db.session.add(obj)
        db.session.commit()
        return obj

    def test_get_director(self, director_service, director):
        assert director_service.get_item(director.id)

    def test_director_not_found(self, director_dao_mock, director_service):
        director_dao_mock.get_by_id.return_value = None

        with pytest.raises(ItemNotFound):
            director_service.get_item(10)

    @pytest.mark.parametrize('page', [1, None], ids=['with page', 'without page'])
    def test_get_director(self, director_dao_mock, director_service, page):
        director = director_service.get_all(page=page)
        assert len(director) == 2
        assert director == director_dao_mock.get_all.return_value
        director_dao_mock.get_all.assert_called_with(page=page)
