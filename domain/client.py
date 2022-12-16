from domain.entity import Entity


class Client(Entity):
    def __init__(self, id_client, name, pin):
        super().__init__(id_client)
        self.__name = name
        self.__pin = pin
        
    def get_name(self):
        return self.__name
    
    def get_pin(self):
        return self.__pin
    
    def set_name(self, name):
        self.__name = name
        
    def set_pin(self, pin):
        self.__pin = pin
        
    def __str__(self):
        return f'id: {self.get_id_entity}, name: {self.__name}, ' \
               f'pin: {self.__pin}'