from unittest.mock import patch

import pytest

from project.exceptions import ItemNotFound
from project.dao.model.movie import Movie
from project.services import MovieService


class TestMovieService:

    @pytest.fixture()
    @patch('project.dao.MovieDAO')
    def movie_dao_mock(self, dao_mock):
        dao = dao_mock()
        dao.get_by_id.return_value = Movie(
            director_id=1,
            genre_id=17,
            description="Владелец ранчо пытается сохранить землю своих предков. Кевин Костнер в неовестерне от автора «Ветреной реки»",
            year=2018,
            title="Йеллоустоун",
            trailer="https://www.youtube.com/watch?v=UKei_d0cbP4",
            rating=8.6
        )
        dao.get_all.return_value = [
            Movie(
                director_id=1,
                genre_id=17,
                description="Владелец ранчо пытается сохранить землю своих предков. Кевин Костнер в неовестерне от автора «Ветреной реки»",
                year=2018,
                title="Йеллоустоун",
                trailer="https://www.youtube.com/watch?v=UKei_d0cbP4",
                rating=8.6
            ),
            Movie(
                director_id=1,
                genre_id=4,
                description="США после Гражданской войны. Легендарный охотник за головами Джон Рут по кличке",
                year=2015,
                title="Омерзительная восьмерка",
                trailer="https://www.youtube.com/watch?v=lmB9VWm0okU",
                rating=7.8
            )
        ]
        return dao

    @pytest.fixture()
    def movie_service(self, movie_dao_mock):
        return MovieService(dao=movie_dao_mock)

    @pytest.fixture
    def movie(self, db):
        obj = Movie(
            director_id=1,
            genre_id=4,
            description="США после Гражданской войны. Легендарный охотник за головами Джон Рут по кличке",
            year=2015,
            title="Омерзительная восьмерка",
            trailer="https://www.youtube.com/watch?v=lmB9VWm0okU",
            rating=7.8
        )
        db.session.add(obj)
        db.session.commit()
        return obj

    def test_get_movie(self, movie_service, movie):
        assert movie_service.get_item(movie.id)

    def test_movie_not_found(self, movie_dao_mock, movie_service):
        movie_dao_mock.get_by_id.return_value = None

        with pytest.raises(ItemNotFound):
            movie_service.get_item(10)

    @pytest.mark.parametrize('page', [1, None], ids=['with page', 'without page'])
    def test_get_movie(self, movie_dao_mock, movie_service, page):
        movie = movie_service.get_all(page=page)
        assert len(movie) == 2
        assert movie == movie_dao_mock.get_all.return_value
        movie_dao_mock.get_all.assert_called_with(page=page)
