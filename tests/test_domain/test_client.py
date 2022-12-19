from domain.client import Client
import unittest


class TestClient(unittest.TestCase):
    def setUp(self):
        self.client = Client(1, "nicu", 1234)
        
    def test_getters(self):
        self.assertTrue(self.client.get_id_entity == 1)
        self.assertTrue(self.client.get_name == "nicu")
        self.assertTrue(self.client.get_pin == 1234)
        self.assertFalse(self.client.get_id_entity == 2)
        self.assertFalse(self.client.get_name == "andrei")
        self.assertFalse(self.client.get_pin == 1235)
        
    def test_setters(self):
        self.client.set_id_entity = 5
        self.assertTrue(self.client.get_id_entity == 5)
        self.client.set_name = "marian"
        self.assertTrue(self.client.get_name == "marian")
        self.client.set_pin = 1234567
        self.assertTrue(self.client.get_pin == 1234567)

    def test_string(self):
        self.client = Client(1, "nicu", 1234)
        self.assertEqual(str(self.client), 'id: 1, name: nicu, pin: 1234')

    def tearDown(self) -> None:
        pass  # cleanup code after each test
