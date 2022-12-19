from repository.repository import Repository
from services.movie_service import MovieService
from domain.exceptions.duplicate_error import DuplicateError
import unittest


class TestMovieService(unittest.TestCase):
    def setUp(self):
        self.movie_repository = Repository()
        self.client_movie_repository = Repository()
        self.movie_service = MovieService(self.movie_repository, self.client_movie_repository)
        
    def test_get_all_movies(self):
        movie_repository = Repository()
        movie_service = MovieService(movie_repository, self.client_movie_repository)
        movie_service.add(1, "John Wick", "description1", "Action")
        movie_service.add(2, "The Matrix", "description2","Sci-Fi")
        movies_list = movie_service.get_all_movies()
        self.assertEqual(len(movies_list), 2)
        
    def test_add(self):
        movie_repository = Repository()
        movie_service = MovieService(movie_repository, self.client_movie_repository)
        movie_service.add(1, "John Wick", "description1", "Action")
        movie_service.add(2, "The Matrix", "description2","Sci-Fi")
        movie_service.add(3, "The Avengers", "description3","Action")
        self.assertRaises(DuplicateError, movie_service.add, 3, "The Avengers", "description3", "Action")
        movies_list = movie_service.get_all_movies()
        self.assertEqual(len(movies_list), 3)
        self.assertEqual(len(movie_repository.get_all()), 3)
        
    def test_modify(self):
        movie_repository = Repository()
        movie_service = MovieService(movie_repository, self.client_movie_repository)
        movie_service.add(1, "John Wick", "description1", "Action")
        movie_service.modify(1, "The Matrix", "description2","Sci-Fi")
        movie = movie_service.get_by_id(1)
        self.assertEqual(movie.get_name, "The Matrix")
        self.assertEqual(movie.get_description, "description2")
        self.assertEqual(movie.get_genre, "Sci-Fi")
        
    def test_remove(self):
        movie_repository = Repository()
        movie_service = MovieService(movie_repository, self.client_movie_repository)
        movie_service.add(1, "John Wick", "description1", "Action")
        movie_service.add(2, "The Matrix", "description2","Sci-Fi")
        movie_service.add(3, "The Avengers", "description3","Action")
        movie_service.remove(2)
        with self.assertRaises(KeyError):
            movie_service.remove(2)
        self.assertEqual(len(movie_service.get_all_movies()), 2)
        self.assertEqual(len(movie_repository.get_all()), 2)
        
    def test_search(self):
        movie_repository = Repository()
        movie_service = MovieService(movie_repository, self.client_movie_repository)
        movie_service.add(1, "John Wick", "description1", "Action")
        movie_service.add(2, "The Matrix", "description2","Sci-Fi")
        movie_service.add(3, "The Avengers", "description3","Action")
        movies_list = movie_service.search("John Wick")
        self.assertEqual(len(movies_list), 1)
        self.assertEqual(movies_list[0].get_name, "John Wick")
        self.assertEqual(movies_list[0].get_description, "description1")
        self.assertEqual(movies_list[0].get_genre, "Action")
        