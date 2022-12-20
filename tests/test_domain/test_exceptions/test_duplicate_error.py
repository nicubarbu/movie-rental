from domain.exceptions.duplicate_error import DuplicateError
import unittest


class TestDuplicateError(unittest.TestCase):
    def setUp(self):
        self.duplicate_error = DuplicateError("DuplicateError")

    def test_duplicate_error(self):
        self.assertEqual(str(self.duplicate_error), "DuplicateError: DuplicateError")
    