from domain.exceptions.name_not_found_error import NameNotFoundError
import unittest


class TestNameNotFoundError(unittest.TestCase):
    def setUp(self):
        self.name_not_found_error = NameNotFoundError("NameNotFoundError")

    def test_name_not_found_error(self):
        self.assertEqual(str(self.name_not_found_error), "NameNotFound: NameNotFoundError")
