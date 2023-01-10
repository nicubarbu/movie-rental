from domain.movie import Movie
import unittest


class TestMovie(unittest.TestCase):
    def setUp(self):
        self.movie = Movie(1, "Avatar", "description", "action")
        
    def test_getters(self):
        self.assertTrue(self.movie.id_entity == 1)
        self.assertFalse(self.movie.id_entity == 2)
        self.assertTrue(self.movie.name == "Avatar")
        self.assertTrue(self.movie.description == "description")
        self.assertTrue(self.movie.genre == "action")
        
    def test_setters(self):
        self.movie.id_entity = 7
        self.assertTrue(self.movie.id_entity == 7)
        self.movie.name = "Coco"
        self.assertFalse(self.movie.name == "Avatar")
        self.movie.genre = "Comedy"
        self.assertFalse(self.movie.genre == "Action")
        self.movie.description = "Lorem Ipsum"
        self.assertTrue(self.movie.description == "Lorem Ipsum")
    
    def test_string(self):
        self.assertEqual(str(self.movie), 'id: 1, title: Avatar, description: description, genre: action')
        
    def tearDown(self) -> None:
        pass  # cleanup code after each test
