from domain.entity import Entity


class ClientMovie(Entity):
    def __init__(self, id_client_movie, id_client, id_movie):
        super().__init__(id_client_movie)
        self.__id_client = id_client
        self.__id_movie = id_movie
        
    @property
    def get_id_client(self):
        return self.__id_client
    
    @property
    def get_id_movie(self):
        return self.__id_movie
    
    @get_id_client.setter
    def set_id_client(self, id_client):
        self.__id_client = id_client
     
    @get_id_movie.setter   
    def set_id_movie(self, id_movie):
        self.__id_movie = id_movie
        
    def __str__(self):
        return f'id: {self.get_id_entity}, ' \
               f'client id: {self.__id_client}, ' \
               f'movie id: {self.__id_movie}'
    