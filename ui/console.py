from domain.exceptions.duplicate_error import DuplicateError
from services.client_service import ClientService
from services.client_movie_service import RentService
from services.movie_service import MovieService
from services.reports import ReportsService
import json


class Console:
    def __init__(self,
                 client_service: ClientService,
                 movie_service: MovieService,
                 client_movie_service: RentService,
                 reports: ReportsService
                 ):
        self.__client_service = client_service
        self.__client_movie_service = client_movie_service
        self.__movie_service = movie_service
        self.__reports = reports
        
    def print_all_clients(self):
        clients = self.__client_service.get_all_clients()
        if len(clients) == 0:
            print("There are no clients!")
        else:
            for client in clients:
                print(client)
                
    def print_all_movies(self):
        movies = self.__movie_service.get_all_movies()
        if len(movies) == 0:
            print("There are no movies!")
        else:
            for movie in movies:
                print(movie)
                
    def print_all_inputs(self):
        inputs = self.__client_movie_service.get_all_inputs()
        if len(inputs) == 0:
            print("There are no active rentals!")
        else:
            for input in inputs:
                print(input)
        
    def print(self, entities):
        for entity in entities:
            print(entity)
        
    def add_client(self):
        try:
            id_client = int(input("Client ID: "))
            name = input("Client name: ")
            pin = int(input("Client PIN: "))
            self.__client_service.add(id_client, name, pin)
        except KeyError as ke:
            print(ke)
        except DuplicateError as de:
            print(de)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)
            
    def modify_client(self):
        try:
            if len(self.__client_service.get_all_clients()) == 0:
                print("There are no clients to modify!")
            else:
                self.print_all_clients()
                id_client = int(input("Client ID: "))
                new_name = input("New name: ")
                new_pin = int(input("New pin: "))
                self.__client_service.modify(id_client, new_name, new_pin)
        except KeyError as ke:
            print(ke)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)
            
    def remove_client(self):
        try:
            if len(self.__client_service.get_all_clients()) == 0:
                print("There are no clients to modify!")
            else:
                self.print_all_clients()
                id_client = int(input("Client ID: "))
                self.__client_service.remove(id_client)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)
            
    def add_movie(self):
        try:
            id_movie = int(input("Movie ID: "))
            name = input("Title: ")
            description = input("Description: ")
            genre = input("Genre: ")
            self.__movie_service.add(id_movie, name, description, genre)
        except DuplicateError as de:
            print(de)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)
            
    def modify_movie(self):
        try:
            if len(self.__movie_service.get_all_movies()) == 0:
                print("There are no movies to modify!")
            else:
                self.print_all_movies()
                id_movie = int(input("Movie ID: "))
                new_name = input("New title: ")
                new_description = input("New description: ")
                new_genre = input("New genre: ")
                self.__movie_service.modify(id_movie, new_name, new_description, new_genre)
        except KeyError as ke:
            print(ke)
        except ValueError as ve:
            print (ve)    
        except Exception as e:
            print(e)
            
    def remove_movie(self):
        try:
            if len(self.__movie_service.get_all_movies()) == 0:
                print("There are no movies to modify!")
            else:
                self.print_all_movies()
                id_movie = int(input("Movie ID: "))
                self.__movie_service.remove(id_movie)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)
        
    def search_client(self):
        try:
            if len(self.__client_service.get_all_clients()) == 0:
                print("There are no clients to search!")
            else:
                name = input("Client name: ")
                clients = self.__client_service.search(name)
                if len(clients) == 0:
                    print("No clients found!")
                else:
                    self.print(clients)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)
        
    def search_movie(self):
        try:
            if len(self.__movie_service.get_all_movies()) == 0:
                print("There are no movies to search!")
            else:
                name = input("Movie title: ")
                movies = self.__movie_service.search(name)
                if len(movies) == 0:
                    print("No movies found!")
                else:
                    self.print(movies)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)
        
    def rent_movie(self):
        try:
            if len(self.__client_service.get_all_clients()) == 0:
                print("There are no clients available!")
            elif len(self.__movie_service.get_all_movies()) == 0:
                print("There are no movies available!")
            else:
                print("Available clients:")
                self.print_all_clients()
                print("\nAvailable movies:")
                self.print_all_movies()
                print("\nCurrent rentals:")
                self.print_all_inputs()
                id_client_movie = int(input("Client-Movie ID: "))
                id_client = int(input("Client ID: "))
                id_movie = int(input("Movie ID: "))
                self.__client_movie_service.add(id_client_movie, id_client, id_movie)
        except KeyError as ke:
            print(ke)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)    
        
    def return_movie(self):
        try:
            if len(self.__client_service.get_all_clients()) == 0:
                print("There are no clients available!")
            elif len(self.__movie_service.get_all_movies()) == 0:
                print("There are no movies available!")
            else:
                print("Active rentals:")
                self.print_all_inputs()
                id_rent = input("Rent ID: ")
                # id_client = int(input("Client ID: "))
                # id_movie = int(input("Movie ID: "))
                self.__client_movie_service.remove(id_rent)
        except KeyError as ke:
            print(ke)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)
        
    def print_reports_client_movie_by_number_of_movies(self):
        try:
            if len(self.__client_service.get_all_clients()) == 0:
                print("There are no clients available!")
            elif len(self.__movie_service.get_all_movies()) == 0:
                print("There are no movies available!")
            else:
                clients = self.__reports.reports_client_movie_by_number_of_movies()
                # print(json.dumps(clients, indent=2))
                print (clients)
        except KeyError as ke:
            print(ke)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)
        
    def print_reports_the_most_rented_movies(self):
        try:
            if len(self.__movie_service.get_all_movies()) == 0:
                print("There are no movies available!")
            else:
                movies = self.__reports.reports_the_most_rented_movies()
                print(json.dumps(movies, indent=2))
        except KeyError as ke:
            print(ke)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)        
        
    def print_reports_top_30_clients(self):
        try:
            if len(self.__client_service.get_all_clients()) == 0:
                print("There are no clients available!")
            elif len(self.__movie_service.get_all_movies()) == 0:
                print("There are no movies available!")
            else:
                clients = self.__reports.reports_top_30_clients()
                print(json.dumps(clients, indent=2))
        except KeyError as ke:
            print(ke)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)
        
        
    def print_menu(self):
        print("""
                ADDITION, MODIFICATION & DELETION
            1. Add client
            2. Modify client
            3. Delete client
            4. Add movie
            5. Modify movie
            6. Delete movie
            
                            SEARCH
            7. Search client
            8. Search movie
            
                            RENTAL & RETURN
            9. Rent movie
            10. Return movie
            
                            REPORTS
            11. Reports for clients who rented movies ordered by the number of rented movies
            12. Reports for the most rented movies
            13. Reports for top 30% clients who rented the most movies
            
                            PRINT
            c. Print all clients
            m. Print all movies
            a. Print all active rentals
            
            x. Exit
            """)
    
    def menu(self):
        
        while True:
            self.print_menu()
            option = input("Option: ")
            if option == '1':
                self.add_client()
            elif option == '2':
                self.modify_client()
            elif option == '3':
                self.remove_client()
            elif option == '4':
                self.add_movie()
            elif option == '5':
                self.modify_movie()
            elif option == '6':
                self.remove_movie()
            elif option == '7':
                self.search_client()
            elif option == '8':
                self.search_movie()
            elif option == '9':
                self.rent_movie()
            elif option == '10':
                self.return_movie()
            elif option == '11':
                self.print_reports_client_movie_by_number_of_movies()
            elif option == '12':
                self.print_reports_the_most_rented_movies()
            elif option == '13':
                self.print_reports_top_30_clients()
            elif option == 'x':
                break
            elif option == 'c':
                self.print_all_clients()
            elif option == 'm':  
                self.print_all_movies()
            elif option == 'a':
                self.print_all_inputs()
            else:
                print("Invalid option!")
                self.print_menu()
            