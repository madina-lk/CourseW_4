from project.config import config
from project.dao.model.genre import Genre
from project.dao.model.director import Director
from project.dao.model.movie import Movie
from project.server import create_app, db

app = create_app(config)

# app.debug = True
#
# if __name__ == '__main__':
#     app.run(host="localhost", port=10001, debug=True)


# @app.shell_context_processor
# def shell():
#     return {
#         "db": db,
#         "Genre": Genre,
#         "Director": Director,
#         "Movie": Movie
#     }
