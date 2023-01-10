from domain.client_movie import ClientMovie
import unittest


class TestClientMovie(unittest.TestCase):
    def setUp(self):
        self.client_movie = ClientMovie(1, 1, 1)
        
    def test_getters(self):
        self.assertTrue(self.client_movie.id_entity == 1)
        self.assertTrue(self.client_movie.id_client == 1)
        self.assertTrue(self.client_movie.id_movie == 1)
        
    def test_setters(self):
        self.client_movie.id_entity = 7
        self.assertTrue(self.client_movie.id_entity == 7)
        self.client_movie.id_client = 2
        self.assertTrue(self.client_movie.id_client == 2)
        self.client_movie.id_movie = 3
        self.assertTrue(self.client_movie.id_movie == 3)
        
    def test_string(self):
        self.assertEqual(str(self.client_movie), 'id: 1, client id: 1, movie id: 1')
        