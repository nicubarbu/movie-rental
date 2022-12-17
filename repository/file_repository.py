from domain.client import Client
from domain.movie import Movie
from repository.repository import Repository


class FileClientRepository(Repository):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
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
            with open(self.__file_name, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    id_client = line.split()[0]
                    name = line.split()[1]
                    pin = line.split()[2]
                    client = Client(int(id_client), name, pin)
                    self._entities[client.get_pin] = client
        except IOError:
            raise IOError("File could not be opened!")
        
    def __write_file(self):
        with open(self.__file_name, 'w') as f:
            for client in self.get_all():
                f.write(f'{client.get_id_entity} {client.get_name} {client.get_pin}')
                
    
class FileMovieRepository(Repository):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self.__read_file()
        
    def add(self, movie):
        super().add(movie)
        self.__write_file()
        
    def modify(self, movie):
        super().modify(movie)
        self.__write_file()
        
    def remove(self, id_movie):
        super().remove(id_movie)
        self.__write_file()
        
    def __read_file(self):
        try:
            with open(self.__file_name, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    id_movie = line.split()[0]
                    title = line.split()[1]
                    description = line.split()[2]
                    genre = line.split()[3]
                    movie = Movie(int(id_movie), title, description, genre)
                    self._entities[movie.get_id_entity] = movie
        except IOError:
            raise IOError("File could not be opened!")
        
    def __write_file(self):
        with open(self.__file_name, 'w') as f:
            for movie in self.get_all():
                f.write(f'{movie.get_id_entity} {movie.get_title} {movie.get_description} {movie.get_genre}')
    