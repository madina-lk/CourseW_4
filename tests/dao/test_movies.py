import pytest

from project.dao import MovieDAO
from project.dao.model.movie import Movie


class TestMovieDAO:

    @pytest.fixture
    def movie_dao(self, db):
        return MovieDAO(db.session)

    @pytest.fixture
    def movie_1(self, db):
        g = Movie(
            director_id=1,
            genre_id=17,
            description="Владелец ранчо пытается сохранить землю своих предков. Кевин Костнер в неовестерне от автора «Ветреной реки»",
            year=2018,
            title="Йеллоустоун",
            trailer="https://www.youtube.com/watch?v=UKei_d0cbP4",
            rating=8.6
        )
        db.session.add(g)
        db.session.commit()
        return g

    @pytest.fixture
    def movie_2(self, db):
        g = Movie(
            director_id=1,
            genre_id=4,
            description="США после Гражданской войны. Легендарный охотник за головами Джон Рут по кличке",
            year=2015,
            title="Омерзительная восьмерка",
            trailer="https://www.youtube.com/watch?v=lmB9VWm0okU",
            rating=7.8
        )
        db.session.add(g)
        db.session.commit()
        return g

    def test_get_movie_by_id(self, movie_1, movie_dao):
        assert movie_dao.get_by_id(movie_1.id) == movie_1

    def test_get_movie_by_id_not_found(self, movie_dao):
        assert not movie_dao.get_by_id(1)

    def test_get_all_movie(self, movie_dao, movie_1, movie_2):
        assert movie_dao.get_all() == [movie_1, movie_2]

    def test_get_movie_by_page(self, app, movie_dao, movie_1, movie_2):
        app.config['ITEMS_PER_PAGE'] = 1
        assert movie_dao.get_all(page=1) == [movie_1]
        assert movie_dao.get_all(page=2) == [movie_2]
        assert movie_dao.get_all(page=3) == []
