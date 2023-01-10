from domain.client import Client
from repository.client_file_repository import FileClientRepository
import pathlib
import os
import unittest

TESTDATA_FILENAME: str = os.path.join(pathlib.Path(__file__).parent.absolute(), 'test.txt')


class TestFileClientRepository(unittest.TestCase):
    def setUp(self):
        self.testfile = open(TESTDATA_FILENAME)
        self.testdata = self.testfile.read()

    def tearDown(self):
        self.testfile.close()
        with open(TESTDATA_FILENAME, mode='w'):
            pass

    def test_add(self):
        repo = FileClientRepository(TESTDATA_FILENAME)
        repo.add(Client(1, 'name', 'pin'))
        self.assertEqual(len(repo.get_all()), 1)
        
    def test_modify(self):
        repo = FileClientRepository(TESTDATA_FILENAME)
        repo.add(Client(1, 'name', 'pin'))
        repo.modify(Client(1, 'name2', 'pin2'))
        with self.assertRaises(KeyError):
            repo.modify(Client(2, 'name2', 'pin2'))
        self.assertEqual(repo.get_all()[0].name, 'name2')
        self.assertEqual(repo.get_all()[0].pin, 'pin2')
        
    def test_remove(self):
        repo = FileClientRepository(TESTDATA_FILENAME)
        repo.add(Client(1, 'name', 'pin'))
        repo.remove(1)
        self.assertEqual(len(repo.get_all()), 0)
        
    def test_read_from_file(self):
        TESTDATA_FILENAME: str = os.path.join(pathlib.Path(__file__).parent.absolute(), 'clients.txt')
        self.testfile = open(TESTDATA_FILENAME)
        self.testdata = self.testfile.read()
        repo = FileClientRepository(TESTDATA_FILENAME)
        self.assertEqual(repo.get_all()[0].name, 'nicu')

    def test_not_exists(self):
        try:
            repo = FileClientRepository("")
            # assert False, "repo should throw exception if file doesn't exist"
        except IOError:
            pass
