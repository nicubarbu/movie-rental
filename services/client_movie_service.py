from domain.client_movie import ClientMovie
from domain.exceptions.duplicate_error import DuplicateError
from domain.exceptions.name_not_found_error import NameNotFoundError
from repository.repository import Repository


class ClientMovieService:
    def __init__(self, client_movie_repository: Repository,
                 client_repository: Repository,
                 movie_repository: Repository):
        self.__client_movie_repository = client_movie_repository
        self.__client_repository = client_repository
        self.__movie_repository = movie_repository
        
    def add(self, id_client_movie, client_name, movie_title):
        if self.__client_repository.get_name(client_name) is None:
            raise NameNotFoundError("There is no client having this name!")
        if self.__movie_repository.get_name(movie_title) is None:
            raise NameNotFoundError("There is no movie having this title!")
        
        inputs = self.__client_movie_repository.get_all()
        for input in inputs:
            if input.get_client_name == client_name and \
                input.get_movie_title == movie_title:
                raise DuplicateError("The client has already rented this movie!")
        
        input = ClientMovie(id_client_movie, client_name, movie_title)
        self.__client_movie_repository.add(input)
        
    # def add(self, id_client_movie, id_client, id_movie):
    #     if self.__client_repository.get_by_id(id_client) is None:
    #         raise KeyError("There is no client having this ID!")
    #     if self.__movie_repository.get_by_id(id_movie) is None:
    #         raise KeyError("There is no movie having this ID!")
        
    #     inputs = self.__client_movie_repository.get_all()
    #     for input in inputs:
    #         if input.get_id_client == id_client and \
    #             input.get_id_movie == id_movie:
    #             raise DuplicateError("The client has already rented this movie!")
                
    #     input = ClientMovie(id_client_movie, id_client, id_movie)
    #     self.__client_movie_repository.add(input)
        
    def get_all_inputs(self):
        return self.__client_movie_repository.get_all()
    
    def remove(self, id_client, id_movie):
        inputs = self.__client_movie_repository.get_all()
        for input in inputs:
            if input.get_id_client == id_client and \
                input.get_id_movie == id_movie:
                self.__client_movie_repository.remove(input.get_id_entity)
                    
            