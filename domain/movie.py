from domain.entity import Entity


class Movie(Entity):
    def __init__(self, id_movie, name, description, genre):
        super().__init__(id_movie)
        self.__name = name
        self.__description = description
        self.__genre = genre
    
    @property    
    def get_name(self):
        return self.__name
    
    @property
    def get_description(self):
        return self.__description
    
    @property
    def get_genre(self):
        return self.__genre
    
    @get_name.setter
    def set_name(self, name):
        self.__name = name
     
    @get_description.setter   
    def set_description(self, description):
        self.__description = description
    
    @get_genre.setter    
    def set_genre(self, genre):
        self.__genre = genre
        
    def __str__(self):
        return f'id: {self.get_id_entity}, title: {self.__name}, ' \
               f'description: {self.__description}, genre: {self.__genre}'