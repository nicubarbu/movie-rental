from domain.client import Client
from repository.repository import Repository


class ClientService:
    def __init__(self, client_repository: Repository,
                 client_movie_repository: Repository):
        self.__client_repository = client_repository
        self.__client_movie_repository = client_movie_repository
        
    def get_all_clients(self):
        '''
        return all clients as list
        input: -
        return: Client type objects list
        '''
        return self.__client_repository.get_all()
    
    def add(self, id_client, name, pin):
        '''
        add a client
        input: id_client - int
               name - string
        return: -
        '''
        client = Client(id_client, name, pin)
        self.__client_repository.add(client)
        
    def modify(self, id_client, new_name, new_pin):
        '''
        modify a client by ID
        input: id_client - int
               new_name - string
               new_pin - int
        return: -
        '''
        new_client = Client(id_client, new_name, new_pin)
        self.__client_repository.modify(new_client)
        
    def remove(self, id_client):
        '''
        remove a client by ID
        input: id_client - int
        return: -
        '''
        clients = self.__client_movie_repository.get_all()
        for client in clients:
            if client.get_id_client() == id_client:
                self.__client_movie_repository.remove(client.get_id_entity())
        self.__client_repository.pop(id_client)
    