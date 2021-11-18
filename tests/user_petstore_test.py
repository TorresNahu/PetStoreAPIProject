import requests
from assertpy import soft_assertions

from pet_store.user.user_petstore import UserPetStore
from tests.assertions.petstore_assertions import *

user = UserPetStore()
status_OK = requests.codes.ok


def test_create_new_user(create_user_data):
    new_username, response = user.create_user(create_user_data)
    assert_response_status_code_is_valid(response, status_OK)
    get_user_response = user.get_user_by_username(new_username)
    with soft_assertions():
        assert_response_status_code_is_valid(get_user_response, status_OK)
        assert_create_new_user_is_successful(get_user_response, new_username)


def test_delete_user(create_user_data):
    new_username, response = user.create_user(create_user_data)
    with soft_assertions():
        assert_response_status_code_is_valid(response, status_OK)
        delete_response = user.delete_user(new_username)
        assert_response_status_code_is_valid(delete_response, status_OK)


def test_login_and_logout_with_user(create_user_data):
    user.create_user(create_user_data)
    username = create_user_data['username']
    password = create_user_data['password']
    login_response = user.login_user_into_the_system(username, password)
    with soft_assertions():
        assert_response_status_code_is_valid(login_response, status_OK)
        assert_that(login_response.as_dict['message']).contains('logged in user session')
        logout_response = user.logout_user_into_the_system()
        assert_response_status_code_is_valid(logout_response, status_OK)
