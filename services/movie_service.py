from domain.movie import Movie
from repository.repository import Repository


class MovieService:
    def __init__(self, movie_repository: Repository):
        self.__movie_repository = movie_repository

    def get_all_movies(self):
        '''
        return all movies as list
        input: -
        return: Movie type objects list
        '''
        return self.__movie_repository.get_all()

    def get_by_id(self, id_movie):
        '''
        return a movie by id
        input: id_movie - int
        return: Movie type object
        '''
        return self.__movie_repository.get_by_id(id_movie)

    def add(self, id_movie, name, description, genre):
        '''
        add a movie
        input: id_movie - int
               name - string
               description - string
               genre - string
        output: -
        '''
        movie = Movie(id_movie, name, description, genre)
        self.__movie_repository.add(movie)

    def modify(self, id_movie, new_name, new_description, new_genre):
        '''
        modify a movie
        input: id_movie - int
               new_name - string
               new_description - string
               new_genre - string
        output: -
        '''
        movie = Movie(id_movie, new_name, new_description, new_genre)
        self.__movie_repository.modify(movie)

    def remove(self, id_movie):
        '''
        remove a movie
        input: id_movie - int
        return: -
        '''
        self.__movie_repository.remove(id_movie)

    def search(self, name):
        '''
        search movies by name
        input: name - string
        return: Movie type objects list
        '''
        movies = self.__movie_repository.get_all()
        movies_found = []
        for movie in movies:
            if name in movie.name:
                movies_found.append(movie)
        return movies_found
