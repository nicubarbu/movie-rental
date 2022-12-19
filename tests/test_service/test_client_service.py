from repository.repository import Repository
from services.client_service import ClientService
from domain.exceptions.duplicate_error import DuplicateError
import unittest


class TestClientService(unittest.TestCase):
    def setUp(self):
        self.client_repository = Repository()
        self.client_movie_repository = Repository()
        self.client_service = ClientService(self.client_repository, self.client_movie_repository)

    def test_get_all_clients(self):
        client_repository = Repository()
        client_service = ClientService(client_repository, self.client_movie_repository)
        client_service.add(1, "John", "1234")
        client_service.add(2, "Nick", "12345")
        clients_list = client_service.get_all_clients()
        self.assertEqual(len(clients_list), 2)

    def test_add(self):
        client_repository = Repository()
        client_service = ClientService(client_repository, self.client_movie_repository)
        client_service.add(1, "John", "1234")
        client_service.add(2, "Nick", "12345")
        client_service.add(3, "Mike", "123456")
        self.assertRaises(DuplicateError, client_service.add, 3, "Mike", "123456")
        clients_list = client_service.get_all_clients()
        self.assertEqual(len(clients_list), 3)
        self.assertEqual(len(client_repository.get_all()), 3)
        
    def test_modify(self):
        client_repository = Repository()
        client_service = ClientService(client_repository, self.client_movie_repository)
        client_service.add(1, "John", "1234")
        client_service.modify(1, "Nick", "12345")
        client = client_service.get_by_id(1)
        self.assertEqual(client.get_name, "Nick")
        self.assertEqual(client.get_pin, "12345")
        
    def test_remove(self):
        client_repository = Repository()
        client_service = ClientService(client_repository, self.client_movie_repository)
        client_service.add(1, "John", "1234")
        client_service.add(2, "Nick", "12345")
        client_service.add(3, "Mike", "123456")
        client_service.remove(2)
        with self.assertRaises(KeyError):
            client_service.remove(2)
        self.assertEqual(len(client_service.get_all_clients()), 2)
        self.assertEqual(len(client_repository.get_all()), 2)
        
    def test_search(self):
        client_repository = Repository()
        client_service = ClientService(client_repository, self.client_movie_repository)
        client_service.add(1, "John", "1234")
        client_service.add(2, "Nick", "12345")
        client_service.add(3, "Mike", "123456")
        self.assertTrue(client_service.search("Nick"))
        