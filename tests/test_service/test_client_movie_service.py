from repository.repository import Repository
from services.client_movie_service import RentService
from domain.exceptions.duplicate_error import DuplicateError
import unittest
import pathlib
import os


class TestClientMovieService(unittest.TestCase):
    def setUp(self):
        self.client_movie_repository = Repository()
        self.client_movie_service = RentService(self.client_movie_repository)

    def test_add(self):
        self.client_movie_service.add(1, 1, 1)
        self.client_movie_service.add(2, 1, 2)
        self.assertRaises(DuplicateError, self.client_movie_service.add, 2, 1, 2)
        rents = self.client_movie_service.get_all_inputs()
        self.assertEqual(len(rents), 2)

    def test_remove(self):
        TESTDATA_FILENAME: str = os.path.join(pathlib.Path(__file__).parent.absolute(), 'clients_movie.txt')
        self.testfile = open(TESTDATA_FILENAME)
        self.client_movie_service.add(500, 10, 5)
        rents = self.client_movie_service.get_all_inputs()
        self.assertEqual(len(rents), 1)
        # self.client_movie_service.remove(500)
        # rents = self.client_movie_service.get_all_inputs()
        # self.assertEqual(len(rents), 0)
        # self.testfile.close()
