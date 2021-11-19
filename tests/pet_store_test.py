import requests as requests
from assertpy.assertpy import soft_assertions

from pet_store.pet.pet_object import PetObject
from tests.assertions.petstore_assertions import *

pet = PetObject()


def test_add_new_pet_to_store(create_pet_data):
    pet.add_new_pet_to_the_store(create_pet_data)
    excepted_pet_id = create_pet_data['id']
    pets = pet.get_pet_by_id(excepted_pet_id)
    with soft_assertions():
        assert_response_status_code_is_valid(pets, requests.codes.ok)
        assert_add_new_pet_is_successful(pets, excepted_pet_id)


def test_update_existing_pet(create_pet_data):
    pet_id, _ = pet.add_new_pet_to_the_store(create_pet_data)
    expected_update_pet_name = "Updated Pet Name"
    create_pet_data['name'] = expected_update_pet_name
    updated_pet_response = pet.update_existing_pet(create_pet_data)
    with soft_assertions():
        assert_response_status_code_is_valid(updated_pet_response, requests.codes.ok)
        assert_updated_pet_name(updated_pet_response, expected_update_pet_name)


def test_delete_pet(create_pet_data):
    unique_pet_id, _ = pet.add_new_pet_to_the_store(create_pet_data)
    delete_pet_response = pet.delete_a_pet(unique_pet_id)
    with soft_assertions():
        assert_response_status_code_is_valid(delete_pet_response, requests.codes.ok)
        is_pet_deleted = pet.get_pet_by_id(unique_pet_id)
        assert_response_status_code_is_valid(is_pet_deleted, requests.codes.not_found)
