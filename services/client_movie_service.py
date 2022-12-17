from domain.client_movie import ClientMovie
from domain.exceptions.duplicate_error import DuplicateError
from repository.repository import Repository


class ClientMovieService:
    def __init__(self, client_movie_repository: Repository,
                 client_repository: Repository,
                 movie_repository: Repository):
        self.__client_movie_repository = client_movie_repository
        self.__client_repository = client_repository
        self.__movie_repository = movie_repository
        
    def add_input(self, id_client_movie, id_client, id_movie):
        if self.__client_repository.get_by_id(id_client) is None:
            raise KeyError("There is no client having this ID!")
        if self.__movie_repository.get_by_id(id_movie) is None:
            raise KeyError("There is no movie having this ID!")
        
        inputs = self.__client_movie_repository.get_all()
        for input in inputs:
            if input.get_id_client == id_client and \
                input.get_id_movie == id_movie:
                raise DuplicateError("The client already rented this movie!")
                
        input = ClientMovie(id_client_movie, id_client, id_movie)
        self.__client_movie_repository.add(input)
        
    def get_all_inputs(self):
        return self.__client_movie_repository.get_all()
    
    def remove_input(self, id_client, id_movie):
        inputs = self.__client_movie_repository.get_all()
        for input in inputs:
            if input.get_id_client == id_client and \
                input.get_id_movie == id_movie:
                self.__client_movie_repository.remove(input.get_id_entity)
                    
            