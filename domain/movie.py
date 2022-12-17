from domain.entity import Entity


class Movie(Entity):
    def __init__(self, id_movie, title, description, genre):
        super().__init__(id_movie)
        self.__title = title
        self.__description = description
        self.__genre = genre
        
    def get_title(self):
        return self.__title
    
    def get_description(self):
        return self.__description
    
    def get_genre(self):
        return self.__genre
    
    def set_title(self, title):
        self.__title = title
        
    def set_description(self, description):
        self.__description = description
        
    def set_genre(self, genre):
        self.__genre = genre
        
    def __str__(self):
        return f'id: {self.get_id_entity}, title: {self.__title}, ' \
               f'description: {self.__description}, genre: {self.__genre}'