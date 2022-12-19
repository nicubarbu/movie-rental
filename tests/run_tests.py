import unittest

from tests.test_domain.test_client import TestClient
from tests.test_domain.test_movie import TestMovie
from tests.test_domain.test_entity import TestEntity
from tests.test_domain.test_client_movie import TestClientMovie
from tests.test_repository.test_repository import TestRepository
from tests.test_service.test_client_service import TestClientService
from tests.test_service.test_movie_service import TestMovieService


def run_tests():
    loader = unittest.defaultTestLoader
    all_suites = \
        [
            loader.loadTestsFromTestCase(TestClient),
            loader.loadTestsFromTestCase(TestMovie),
            loader.loadTestsFromTestCase(TestEntity),
            loader.loadTestsFromTestCase(TestClientMovie),
            # loader.loadTestsFromTestCase(TestRepository),
            loader.loadTestsFromTestCase(TestClientService),
            loader.loadTestsFromTestCase(TestMovieService)
        ]
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(unittest.TestSuite(all_suites))


if __name__ == '__main__':
    run_tests()
