from repository.repository import Repository
from services.client_service import ClientService
from services.client_movie_service import ClientMovieService
from services.movie_service import MovieService
# from tests.
from ui.console import Console


def main():

    client_repository = Repository()
    client_movie_repository = Repository()
    movie_repository = Repository()
    
    client_service = ClientService(client_repository, client_movie_repository)
    movie_service = MovieService(movie_repository, client_movie_repository)
    client_movie_service = ClientMovieService(client_movie_repository, 
                                              client_repository, 
                                              movie_repository)
    
    console = Console(client_service, movie_service, client_movie_service)
    console.menu()


main()
