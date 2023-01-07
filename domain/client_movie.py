from domain.entity import Entity


class ClientMovie(Entity):
    def __init__(self, id_client_movie: int, id_client: int, id_movie: int):
        super().__init__(id_client_movie)
        self.__id_client = id_client
        self.__id_movie = id_movie
        
    @property
    def id_client(self):
        return self.__id_client
    
    @id_client.setter
    def id_client(self, id_client):
        self.__id_client = id_client
    
    @property
    def id_movie(self):
        return self.__id_movie
     
    @id_movie.setter   
    def id_movie(self, id_movie):
        self.__id_movie = id_movie
        
    def __str__(self):
        return f'id: {self.id_entity}, ' \
               f'client id: {self.__id_client}, ' \
               f'movie id: {self.__id_movie}'
