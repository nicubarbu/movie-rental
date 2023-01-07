from domain.client import Client
from repository.repository import Repository
from repository.client_file_repository import FileClientRepository
from repository.movie_file_repository import FileMovieRepository
from repository.client_movie_file_repository import FileClientMovieRepository


class ReportsService:
    def __init__(self, client_service, movie_service):
        self.__client_service = client_service
        self.__movie_service = movie_service

    def reports_client_movie_by_number_of_movies(self):
        with open ('clients_movie.txt', 'r') as file:
            lines = file.readlines()
            clients = {}
            for line in lines:
                parts = line.split()
                id_client = parts[1]
                client_name = self.__client_service.get_by_id(int(id_client)).get_name
                if client_name in clients:
                    clients[client_name] += 1
                else:
                    clients[client_name] = 1
            sorted_clients = dict(sorted(clients.items(), key=lambda item: item[1], reverse=True))
            return sorted_clients
        
    def reports_the_most_rented_movies(self):
        with open ('clients_movie.txt', 'r') as file:
            lines = file.readlines()
            movies = {}
            for line in lines:
                parts = line.split()
                id_movie = parts[2]
                movie_name = self.__movie_service.get_by_id(int(id_movie)).get_name
                if movie_name in movies:
                    movies[movie_name] += 1
                else:
                    movies[movie_name] = 1
            sorted_movies = dict(sorted(movies.items(), key=lambda item: item[1], reverse=True))
            return sorted_movies
        
    def reports_top_30_clients(self):
        # reports_client_movie_by_number_of_movies()
        with open('clients_movie.txt', 'r') as file:
            lines = file.readlines()
            clients = {}
            for line in lines:
                parts = line.split()
                id_client = parts[1]
                client_name = self.__client_service.get_by_id(int(id_client)).get_name
                if client_name in clients:
                    clients[client_name] += 1
                else:
                    clients[client_name] = 1
            sorted_clients = list(sorted(clients.items(), key=lambda item: item[1], reverse=True))
        # until here
            
            top_clients = {}
            percent = int(0.3 * len(sorted_clients))
            for i in range(percent):
                top_clients[sorted_clients[i][0]] = sorted_clients[i][1]

            return top_clients
    