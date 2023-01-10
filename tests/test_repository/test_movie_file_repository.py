from domain.movie import Movie
from repository.movie_file_repository import FileMovieRepository
import pathlib
import os
import unittest

TESTDATA_FILENAME: str = os.path.join(pathlib.Path(__file__).parent.absolute(), 'test.txt')


class TestFileMovieRepository(unittest.TestCase):
    def setUp(self):
        self.testfile = open(TESTDATA_FILENAME)
        self.testdata = self.testfile.read()
        
    def tearDown(self):
        self.testfile.close()
        with open(TESTDATA_FILENAME, mode='w'):
            pass
        
    def test_add(self):
        repo = FileMovieRepository(TESTDATA_FILENAME)
        repo.add(Movie(1, 'Thor', 'description', 'genre'))
        self.assertEqual(len(repo.get_all()), 1)
        
    def test_modify(self):
        repo = FileMovieRepository(TESTDATA_FILENAME)
        repo.add(Movie(1, 'Thor', 'description', 'genre'))
        repo.modify(Movie(1, 'Thor2', 'description2', 'genre2'))
        with self.assertRaises(KeyError):
            repo.modify(Movie(2, 'Thor2', 'description2', 'genre2'))
        self.assertEqual(repo.get_all()[0].name, 'Thor2')
        self.assertEqual(repo.get_all()[0].description, 'description2')
        self.assertEqual(repo.get_all()[0].genre, 'genre2')
        
    def test_remove(self):
        repo = FileMovieRepository(TESTDATA_FILENAME)
        repo.add(Movie(1, 'Thor', 'description', 'genre'))
        repo.remove(1)
        self.assertEqual(len(repo.get_all()), 0)
        
    def test_read_from_file(self):
        TESTDATA_FILENAME: str = os.path.join(pathlib.Path(__file__).parent.absolute(), 'movies.txt')
        self.testfile = open(TESTDATA_FILENAME)
        self.testdata = self.testfile.read()
        repo = FileMovieRepository(TESTDATA_FILENAME)
        self.assertEqual(repo.get_all()[1].name, 'Thor')
        
    def test_not_exists(self):
        try:
            repo = FileMovieRepository("")
            # assert False, "repo should throw exception if file doesn't exist"
        except IOError:
            pass
    