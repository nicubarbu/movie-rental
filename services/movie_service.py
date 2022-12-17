from domain.movie import Movie
from repository.repository import Repository


class MovieService:
    def __init__(self, movie_repository: Repository,
                 client_movie_repository: Repository):
        self.__movie_repository = movie_repository
        self.__client_movie_repository = client_movie_repository
        
    def get_all_movies(self):
        '''
        return all movies as list
        input: -
        return: Movie type objects list
        '''
        return self.__movie_repository.get_all()
    
    def add(self, id_movie, title, description, genre):
        '''
        add a movie
        input: id_movie - int
               title - string
               description - string
               genre - string
        output: -
        '''
        movie = Movie(id_movie, title, description, genre)
        self.__movie_repository.add(movie)
        
    def modify(self, id_movie, new_title, new_description, new_genre):
        '''
        modify a movie
        input: id_movie - int
               new_title - string
               new_description - string
               new_genre - string
        output: -
        '''
        movie = Movie(id_movie, new_title, new_description, new_genre)
        self.__movie_repository.modify(movie)
        
    def remove(self, id_movie):
        '''
        remove a movie
        input: id_movie - int
        return: -
        '''
        inputs = self.__client_movie_repository.get_all()
        for input in inputs:
            if input.get_id_movie() == id_movie:
                self.__client_movie_repository.remove(input.get_id_entity())
        self.__movie_repository.remove(id_movie)
        
    
            
        