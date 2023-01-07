from domain.entity import Entity


class Movie(Entity):
    def __init__(self, id_movie: int, name: str, description: str, genre: str):
        super().__init__(id_movie)
        self.__name = name
        self.__description = description
        self.__genre = genre
    
    @property    
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def description(self):
        return self.__description
    
    @description.setter   
    def description(self, description):
        self.__description = description
    
    @property
    def genre(self):
        return self.__genre
    
    @genre.setter    
    def genre(self, genre):
        self.__genre = genre
        
    def __str__(self):
        return f'id: {self.id_entity}, title: {self.__name}, ' \
               f'description: {self.__description}, genre: {self.__genre}'
