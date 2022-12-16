class Entity:
    def __init__(self, id_entity):
        self.__id_entity = id_entity
        
    @property 
    def get_id_entity(self):
        return self.__id_entity
    
    @get_id_entity.setter
    def set_id_entity(self, id_entity):
        self.__id_entity = id_entity
        