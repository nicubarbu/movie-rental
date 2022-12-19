from repository.repository import Repository
from domain.client import Client
import unittest


class TestRepository(unittest.TestCase):
    # def test_get_name(self):
    #     repo = Repository()
    #     repo.add(Client(1, 'name', 'pin'))
    #     client = repo.get_by_id(1)
    #     self.assertEqual(client.get_name, 'name')
    
    def test_add(self):
        repo = Repository()
        repo.add(Client(1, 'name', 'pin'))
        self.assertEqual(len(repo.get_all()), 1)
        
    def test_modify(self):
        repo = Repository()
        repo.add(Client(1, 'name', 'pin'))
        repo.modify(Client(1, 'name2', 'pin2'))
        with self.assertRaises(KeyError):
            repo.modify(Client(2, 'name2', 'pin2'))
        self.assertEqual(repo.get_all()[0].get_name, 'name2')
        self.assertEqual(repo.get_all()[0].get_pin, 'pin2')
        
    def test_remove(self):
        repo = Repository()
        repo.add(Client(1, 'name', 'pin'))
        repo.remove(1)
        self.assertEqual(len(repo.get_all()), 0)
        
    def test_search(self):
        repo = Repository()
        repo.add(Client(1, 'name', 'pin'))
        self.assertTrue(repo.search('name'))
        self.assertFalse(repo.search('name2'))
    