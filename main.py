from repository.repository import Repository
from repository.file_repository import FileClientRepository, FileMovieRepository
from services.client_service import ClientService
from services.client_movie_service import ClientMovieService
from services.movie_service import MovieService
from ui.console import Console


def main():

    client_file_repository = FileClientRepository("clients.txt")
    movie_file_repository = FileMovieRepository("movies.txt")
    
    client_repository = Repository()
    client_movie_repository = Repository()
    movie_repository = Repository()
    
    client_service = ClientService(client_file_repository, client_movie_repository)
    movie_service = MovieService(movie_file_repository, client_movie_repository)
    client_movie_service = ClientMovieService(client_movie_repository, 
                                              client_file_repository, 
                                              movie_file_repository)
    
    console = Console(client_service, movie_service, client_movie_service)
    console.menu()


main()
