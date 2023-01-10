from domain.exceptions.duplicate_error import DuplicateError


class Repository:
    def __init__(self):
        self._entities = {}
        
    def get_all(self):
        '''
        return entities list
        input: -
        return: objects list of Entity type
        '''
        return list(self._entities.values())
    
    def get_by_id(self, id_entity):
        '''
        return entity with specific id
        input: id_entity - string
        return: if True - Entity type object
                if False - None
        '''
        if id_entity in self._entities:
            return self._entities[id_entity]
        return None
    
    # def get_name(self, name):
    #     '''
    #     return entity with specific name
    #     input: name - string
    #     return: if True - Entity type object
    #             if False - None
    #     '''
    #     for entity in self._entities.values():
    #         if entity.name == name:
    #             return entity
    #     return None
    
    def add(self, entity):
        '''
        add entity to dictionary
        input: entity - Entity type object
        return: -
        '''
        if self.get_by_id(entity.id_entity) is not None:
            raise DuplicateError("It already exists an entity having this ID!")
        self._entities[entity.id_entity] = entity
        
    def modify(self, entity):
        '''
        modify an entity
        input: entity - Entity type object
        return: -
        '''
        if self.get_by_id(entity.id_entity) is None:
            raise KeyError("There is no entity having this ID!")
        self._entities[entity.id_entity] = entity
        
    def remove(self, id_entity):
        '''
        remove an entity by ID
        input: id_entity - string
        return: -
        ''' 
        if self.get_by_id(id_entity) is None:
            raise KeyError("There is no entity having this ID!")
        self._entities.pop(id_entity)
        
    def search(self, name):
        '''
        search an entity by name
        input: name - string
        return: Entity type object
        '''
        for entity in self._entities.values():
            if entity.name == name:
                return entity
        return None
