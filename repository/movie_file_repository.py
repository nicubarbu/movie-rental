from domain.movie import Movie
from repository.repository import Repository


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
                    parts = line.split()
                    id_movie = parts[0]
                    title = parts[1]
                    description = parts[2]
                    genre = parts[3]
                    movie = Movie(int(id_movie), title, description, genre)
                    self._entities[movie.get_id_entity] = movie
        except IOError:
            raise IOError("File could not be opened!")
        
    def __write_file(self):
        with open(self.__file_name, 'w') as f:
            for movie in self.get_all():
                f.write(f'{movie.get_id_entity} {movie.get_name} {movie.get_description} {movie.get_genre}')
                