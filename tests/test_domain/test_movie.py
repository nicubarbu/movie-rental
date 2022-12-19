from domain.movie import Movie
import unittest


class TestMovie(unittest.TestCase):
    def setUp(self):
        self.movie = Movie(1, "Avatar", "description", "action")
        
    def test_getters(self):
        self.assertTrue(self.movie.get_id_entity == 1)
        self.assertFalse(self.movie.get_id_entity == 2)
        self.assertTrue(self.movie.get_name == "Avatar")
        self.assertTrue(self.movie.get_description == "description")
        self.assertTrue(self.movie.get_genre == "action")
        
    def test_setters(self):
        self.movie.set_id_entity = 7
        self.assertTrue(self.movie.get_id_entity == 7)
        self.movie.set_name = "Coco"
        self.assertFalse(self.movie.get_name == "Avatar")
        self.movie.set_genre = "Comedy"
        self.assertFalse(self.movie.get_genre == "Action")
        self.movie.set_description = "Lorem Ipsum"
        self.assertTrue(self.movie.get_description == "Lorem Ipsum")
    
    def test_string(self):
        self.assertEqual(str(self.movie), 'id: 1, title: Avatar, description: description, genre: action')
        
    def tearDown(self) -> None:
        pass  # cleanup code after each test
