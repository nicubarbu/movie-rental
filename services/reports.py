from domain.dto import *
from services.client_movie_service import RentService
from services.client_service import ClientService
from services.movie_service import MovieService

class ReportsService:
    def __init__(self,
                 client_service: ClientService,
                 movie_service: MovieService,
                 client_movie_service: RentService):
        self.__client_service = client_service
        self.__movie_service = movie_service
        self.__client_movie_service = client_movie_service

    def reports_client_movie_by_number_of_movies(self):
        '''
        create reports for clients who rented movies
        ordered by the number of rentals
        '''
        lst = self.__client_movie_service.get_all_inputs()
        clients = {}
        
        for line in lst:
            client_name = self.__client_service.get_by_id(int(line.id_client)).name
            if client_name in clients:
                clients[client_name] += 1
            else:
                clients[client_name] = 1
                
        dto_list = []
        for elem in clients:
            dto_list.append(ClientDTO(elem, clients[elem]))
            
        sorted_dto_list = sorted(dto_list, key=lambda x: x.rent_number, reverse=True)
        return sorted_dto_list
                
        
    def reports_the_most_rented_movies(self):
        '''
        create reports for movies ordered by
        the number of rentals
        '''
        lst = self.__client_movie_service.get_all_inputs()
        movies = {}
        
        for line in lst:
            movie_title = self.__movie_service.get_by_id(int(line.id_movie)).name
            if movie_title in movies:
                movies[movie_title] += 1
            else:
                movies[movie_title] = 1
                
        dto_dict = {}
        for elem in movies:
            dto_dict[elem] = movies[elem]
            
        sorted_dto_dict = dict(sorted(dto_dict.items(), key=lambda item: item[1], reverse=True))
        return sorted_dto_dict
        
    def reports_top_30_clients(self):
        '''
        create reports for top 30% clients
        who rented the most movies
        '''
        number_of_clients = self.__client_service.get_all_clients()
        lst = self.__client_movie_service.get_all_inputs()
        clients = {}
        
        for line in lst:
            client_name = self.__client_service.get_by_id(int(line.id_client)).name
            if client_name in clients:
                clients[client_name] += 1
            else:
                clients[client_name] = 1
                
        dto_dict = {}
        for elem in clients:
            dto_dict[elem] = clients[elem]
        sorted_dto_dict = list(sorted(dto_dict.items(), key=lambda item: item[1], reverse=True))
        
        top_clients = {}
        percent = int(0.3 * len(number_of_clients))
        for i in range(percent):
            top_clients[sorted_dto_dict[i][0]] = sorted_dto_dict[i][1]

        return top_clients
