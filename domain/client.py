from domain.entity import Entity


class Client(Entity):
    def __init__(self, id_client: int, name: str, pin: str):
        super().__init__(id_client)
        self.__name = name
        self.__pin = pin
        
    @property    
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def pin(self):
        return self.__pin
        
    @pin.setter
    def pin(self, pin):
        self.__pin = pin
        
    def __str__(self):
        return f'id: {self.id_entity}, name: {self.__name}, ' \
               f'pin: {self.__pin}'
