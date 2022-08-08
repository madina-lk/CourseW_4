

from typing import Optional

from project.dao.base import BaseDAO
from project.exceptions import ItemNotFound
from project.dao.model.movie import Movie

from typing import List


class MovieService:
    def __init__(self, dao: BaseDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> Movie:
        if genre := self.dao.get_by_id(pk):
            return genre
        raise ItemNotFound(f'Genre with pk={pk} not exists.')

    def get_all(self, page: Optional[int] = None) -> List[Movie]:
        return self.dao.get_all(page=page)

