from json import dumps
from uuid import uuid4

import requests as requests
from assertpy.assertpy import assert_that, soft_assertions
from config import *

################## VARIABLES ##################
_pet_status = {
    "AVAILABLE": "available",
    "PENDING": "pending",
    "SOLD": "sold"
}

################## TESTS ##################


def test_available_pets_has_doggie():
    response = get_all_pets_by_status(_pet_status["AVAILABLE"])
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(requests.codes.ok)
        pets = response.json()
        pet_names = search_pets_by_condition(pets, 'doggie', 'name')
        assert_that(pet_names).is_true()


def test_add_new_pet_to_store():
    unique_pet = create_a_new_unique_pet()
    pets = get_all_pets_by_status(_pet_status["AVAILABLE"]).json()
    is_new_pet_created = search_pets_by_condition(pets, unique_pet['id'], 'id')
    assert_that(is_new_pet_created).is_true()


def test_delete_pet():
    unique_pet = create_a_new_unique_pet()
    url = f'{BASE_URL_PET}{unique_pet["id"]}'
    delete_pet = requests.delete(url=url)
    with soft_assertions():
        assert_that(delete_pet.status_code).is_equal_to(requests.codes.ok)
        is_pet_deleted = get_pet_by_id(unique_pet['id'])
        assert_that(is_pet_deleted.status_code).is_equal_to(requests.codes.not_found)

################## FUNCTIONS ##################


def create_a_new_unique_pet():
    unique_pet_name = f'Pet {str(uuid4())}'
    payload = dumps({
        "id": 0,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": unique_pet_name,
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    })
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    response = requests.post(url=BASE_URL_PET, data=payload, headers=headers)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    return response.json()


def search_pets_by_condition(pets, pet_expected, condition):
    pet_list = []
    for pet in pets:
        if pet[condition] == pet_expected:
            pet_list.append(pet)
            break

    return pet_list


def get_all_pets_by_status(status):
    """
    :param status: Str. Available values : available, pending, sold
    :return: All pets according to a provided status.
    """
    return requests.get(f'{FIND_PET_BY_STATUS_URL}{status}')


def get_pet_by_id(pet_id):
    return requests.get(f'{BASE_URL_PET}{str(pet_id)}')
