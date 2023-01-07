from domain.client_movie import ClientMovie
from domain.exceptions.duplicate_error import DuplicateError
from domain.exceptions.name_not_found_error import NameNotFoundError
from repository.repository import Repository


class RentService:
    def __init__(self, client_movie_repository: Repository):
        self.__client_movie_repository = client_movie_repository
    
    def add(self, id_client_movie, id_client, id_movie):
        inputs = self.__client_movie_repository.get_all()
        for input in inputs:
            if input.get_id_client == id_client and \
                input.get_id_movie == id_movie:
                raise DuplicateError("The client has already rented this movie!")
        
        input = ClientMovie(id_client_movie, id_client, id_movie)
        self.__client_movie_repository.add(input)
        
    def get_all_inputs(self):
        return self.__client_movie_repository.get_all()
    
    def remove(self, id_client, id_movie):
        inputs = self.__client_movie_repository.get_all()
        for input in inputs:
            if input.get_id_client == id_client and \
                input.get_id_movie == id_movie:
                self.__client_movie_repository.remove(input.get_id_entity)
                    