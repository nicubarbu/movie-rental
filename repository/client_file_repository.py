from domain.client import Client
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
                    parts = line.split()
                    id_client = parts[0]
                    name = parts[1]
                    pin = parts[2]
                    client = Client(int(id_client), name, pin)
                    self._entities[client.get_pin] = client
        except IOError:
            raise IOError("File could not be opened!")
        
    def __write_file(self):
        with open(self.__file_name, 'w') as f:
            for client in self.get_all():
                f.write(f'{client.get_id_entity} {client.get_name} {client.get_pin}')
                
    