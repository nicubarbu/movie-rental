from domain.client import Client
import unittest


class TestClient(unittest.TestCase):
    def setUp(self):
        self.client = Client(1, "nicu", 1234)
        
    def test_getters(self):
        self.assertTrue(self.client.id_entity == 1)
        self.assertTrue(self.client.name == "nicu")
        self.assertTrue(self.client.pin == 1234)
        self.assertFalse(self.client.id_entity == 2)
        self.assertFalse(self.client.name == "andrei")
        self.assertFalse(self.client.pin == 1235)
        
    def test_setters(self):
        self.client.id_entity = 5
        self.assertTrue(self.client.id_entity == 5)
        self.client.name = "marian"
        self.assertTrue(self.client.name == "marian")
        self.client.pin = 1234567
        self.assertTrue(self.client.pin == 1234567)

    def test_string(self):
        self.client = Client(1, "nicu", 1234)
        self.assertEqual(str(self.client), 'id: 1, name: nicu, pin: 1234')

    def tearDown(self) -> None:
        pass  # cleanup code after each test
