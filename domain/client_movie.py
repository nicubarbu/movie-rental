from domain.entity import Entity


class ClientMovie(Entity):
    def __init__(self, id_client_movie, id_client, id_movie):
        super().__init__(id_client_movie)
        self.__id_client = id_client
        self.__id_movie = id_movie
        
    def get_id_client(self):
        return self.__id_client
    
    def get_id_movie(self):
        return self.__id_movie
    
    def set_id_client(self, id_client):
        self.__id_client = id_client
        
    def set_id_movie(self, id_movie):
        self.__id_movie = id_movie
        
    def __str__(self):
        return f'id: {self.get_id_entity}, ' \
               f'id client: {self.__id_client}, ' \
               f'id movie: {self.__id_movie}'