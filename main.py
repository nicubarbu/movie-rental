from repository.repository import Repository
from repository.client_file_repository import FileClientRepository
from repository.movie_file_repository import FileMovieRepository
from repository.client_movie_file_repository import FileClientMovieRepository
from services.client_service import ClientService
from services.client_movie_service import ClientMovieService
from services.movie_service import MovieService
from ui.console import Console


def main():

    client_file_repository = FileClientRepository("clients.txt")
    movie_file_repository = FileMovieRepository("movies.txt")
    client_movie_file_repository = FileClientMovieRepository("clients_movie.txt")
    
    client_service = ClientService(client_file_repository, client_movie_file_repository)
    movie_service = MovieService(movie_file_repository, client_movie_file_repository)
    client_movie_service = ClientMovieService(client_movie_file_repository, 
                                              client_file_repository, 
                                              client_movie_file_repository)
    
    console = Console(client_service, movie_service, client_movie_service)
    console.menu()


main()
