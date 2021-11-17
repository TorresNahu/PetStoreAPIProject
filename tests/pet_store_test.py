import requests as requests
from assertpy.assertpy import soft_assertions

import data.pet_status_dict as pet_status_dict
from pet_store.pet.base_pet import BasePet
from tests.assertions.pets_assertions import *

pet = BasePet()


def test_available_pets_has_expected_pet_name(pet_name="doggie"):
    response = pet.get_pets_by_status(pet_status_dict.pet_status.get('AVAILABLE'))
    with soft_assertions():
        assert_response_status_code_is_valid(response, requests.codes.ok)
        # assert_pet_name_exists(response, pet_name)
        pets = response.json()
        # pet_names = search_pets_by_condition(response, 'doggie', 'name')
        # assert_that(pet_names).is_true()


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
