from domain.entity import Entity
import unittest


class TestEntity(unittest.TestCase):
    def setUp(self):
        self.entity = Entity(10)
        
    def test_getters(self):
        self.assertTrue(self.entity.id_entity == 10)
        self.assertFalse(self.entity.id_entity == 2)
    
    def test_setters(self):
        self.entity.id_entity = 7
        self.assertTrue(self.entity.id_entity == 7)
