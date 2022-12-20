from domain.client import Client
from domain.movie import Movie
from domain.client_movie import ClientMovie
from repository.repository import Repository


class FileClientMovieRepository(Repository):
    def __init__(self, file_name_client_movie):
        super().__init__()
        self.__file_name_client_movie = file_name_client_movie
        self.__read_file()
        
    def add(self, client):
        super().add(client)
        self.__write_file()
        
    def modify(self, client):
        super().modify(client)
        self.__write_file()
        
    def remove(self, id_client):
        super().remove(id_client)
        self.__write_file()
        
    def __read_file(self):
        try:
            with open(self.__file_name_client_movie, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    parts = line.split()
                    id_client_movie = parts[0]
                    id_client = parts[1]
                    id_movie = parts[2]
                    client_movie = ClientMovie(int(id_client_movie), int(id_client), int(id_movie))
                    self._entities[client_movie.get_id_entity] = client_movie
        except IOError:
            raise IOError("File could not be opened!")
                    
    def __write_file(self):
        with open(self.__file_name_client_movie, 'w') as f:
            for entity in self.get_all():
                entities = len(self.get_all()) + 1
                f.write(f'{entity.get_id_entity} {entity.get_id_client} {entity.get_id_movie}')
                