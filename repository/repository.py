from domain.exceptions.duplicate_error import DuplicateError


class Repository:
    def __init__(self):
        self.__entities = {}
        
    def get_all(self):
        '''
        return entities list
        input: -
        return: objects list of Entity type
        '''
        return list(self.__entities.values())
    
    def get_by_id(self, id_entity):
        '''
        return entity with specific id
        input: id_entity - string
        return: if True - Entity type object
                if False - None
        '''
        if id_entity in self.__entities:
            return self.__entities[id_entity]
        return None
    
    def add(self, entity):
        '''
        add entity to dictionary
        input: entity - Entity type object
        return: -
        '''
        if self.get_by_id(entity.get_id_entity) is not None:
            raise DuplicateError("It already exists an entity having this ID!")
        self.__entities[entity.get_id_entity] = entity
        
    def modify(self, new_entity):
        '''
        modify an entity
        input: new_entity - Entity type object
        return: -
        '''
        if self.get_by_id(new_entity.get_id_entity()) is None:
            raise KeyError("There is no entity having this ID!")
        self.__entities[new_entity.get_id_entity()] = new_entity
        
    def remove(self, id_entity):
        '''
        remove an entity by ID
        input: id_entity - string
        return: -
        ''' 
        if self.get_by_id(id_entity) is None:
            raise KeyError("There is no entity having this ID!")
        self.__entities.pop(id_entity)
