from domain.movie import Movie
from repository.repository import Repository


class MovieService:
    def __init__(self, movie_repository: Repository,
                 client_movie_repository: Repository):
        self.__movie_repository = movie_repository
        self.__client_movie_repository = client_movie_repository

    def get_all_movies(self):
        '''
        return all movies as list
        input: -
        return: Movie type objects list
        '''
        return self.__movie_repository.get_all()

    def get_by_id(self, id_movie):
        '''
        return a movie by id
        input: id_movie - int
        return: Movie type object
        '''
        return self.__movie_repository.get_by_id(id_movie)

    def add(self, id_movie, name, description, genre):
        '''
        add a movie
        input: id_movie - int
               name - string
               description - string
               genre - string
        output: -
        '''
        movie = Movie(id_movie, name, description, genre)
        self.__movie_repository.add(movie)

    def modify(self, id_movie, new_name, new_description, new_genre):
        '''
        modify a movie
        input: id_movie - int
               new_name - string
               new_description - string
               new_genre - string
        output: -
        '''
        movie = Movie(id_movie, new_name, new_description, new_genre)
        self.__movie_repository.modify(movie)

    def remove(self, id_movie):
        '''
        remove a movie
        input: id_movie - int
        return: -
        '''
        # inputs = self.__client_movie_repository.get_all()
        # for input in inputs:
        #     if input.get_id_movie == id_movie:
        #         self.__client_movie_repository.remove(input.get_id_entity)
        self.__movie_repository.remove(id_movie)

    def search(self, name):
        '''
        search movies by name
        input: name - string
        return: Movie type objects list
        '''
        movies = self.__movie_repository.get_all()
        movies_found = []
        for movie in movies:
            if name in movie.get_name:
                movies_found.append(movie)
        return movies_found

    # def order_movies_by_number_of_clients(self):
    #     '''
    #     order movies by client name
    #     input: -
    #     return: Movie type objects list
    #     '''
    #     number_of_clients_that_rented = {}
    #     inputs = self.__client_movie_repository.get_all()
    #     for input in inputs:
    #         if input.get_name_movie in number_of_clients_that_rented:
    #             number_of_clients_that_rented[input.get_name_movie] += 1
    #         else:
    #             number_of_clients_that_rented[input.get_name_movie] = 1

    #     alphabetically_sorted_movies = sorted(number_of_clients_that_rented,
    #                                           key=lambda name: number_of_clients_that_rented[name])
    #     sorted_movies = []
    #     for movie_title in alphabetically_sorted_movies:
    #         sorted_movies.append((movie_title, number_of_clients_that_rented[movie_title]))
    #     return sorted_movies

    # def order_movies_by_clients(self):
    #     '''
    #     order movies by clients number
    #     input: -
    #     return: Movie type objects list
    #     '''
    #     movies = self.__movie_repository.get_all()
    #     movies_ordered = []
    #     for movie in movies:
    #         clients = self.__client_movie_repository.get_all()
    #         clients_number = 0
    #         for client in clients:
    #             if movie.get_id_entity == client.get_id_movie:
    #                 clients_number += 1
    #         movie.set_clients_number(clients_number)
    #         movies_ordered.append(movie)
    #     movies_ordered.sort(key=lambda x: x.get_clients_number, reverse=True)
    #     return movies_ordered
