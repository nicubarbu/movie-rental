from domain.client_movie import ClientMovie
from repository.repository import Repository


class FileClientMovieRepository(Repository):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self.__read_file()
        
    def add(self, client_movie):
        super().add(client_movie)
        self.__write_file()
        
    def modify(self, client_movie):
        super().modify(client_movie)
        self.__write_file()
        
    def remove(self, id_client_movie):
        super().remove(id_client_movie)
        self.__write_file()
        
    def __read_file(self):
        try:
            with open(self.__file_name, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    parts = line.split()
                    id_client_movie = parts[0]
                    id_client = parts[1]
                    id_movie = parts[2]
                    client_movie = ClientMovie(int(id_client_movie), int(id_client), int(id_movie))
                    self._entities[client_movie.id_entity] = client_movie
        except IOError:
            raise IOError("File could not be opened!")
                    
    def __write_file(self):
        with open(self.__file_name, 'w') as f:
            for entity in self.get_all():
                f.write(f'{entity.id_entity} {entity.id_client} {entity.id_movie}')
                