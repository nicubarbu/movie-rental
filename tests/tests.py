import tests.client.test_client
import tests.client.test_client_repository

import tests.movie.test_movie


def test_all():
    #tests for client
    
    tests.client.test_client.test_client()
    tests.client.test_client.test_client_setters()
    
    tests.client.test_client_repository.test_get_all_repository()
    tests.client.test_client_repository.test_get_by_id_repository()
    tests.client.test_client_repository.test_get_name_repository()
    tests.client.test_client_repository.test_add_repository()
    tests.client.test_client_repository.test_modify_repository()
    tests.client.test_client_repository.test_remove_repository()
    tests.client.test_client_repository.test_search_repository()
    
    
    