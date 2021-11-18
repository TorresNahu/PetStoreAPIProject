import random

import pytest
from utils.file_reader import read_file


@pytest.fixture
def create_pet_data():
    payload = read_file('create_pet.json')
    random_pet_id = random.randrange(000000000000000000, 999999999999999999)
    unique_pet_id = random_pet_id

    payload['id'] = unique_pet_id
    yield payload


@pytest.fixture
def create_user_data():
    payload = read_file('create_user.json')
    user_username = f'Test user {random.randrange(00000, 99999)}'
    payload['username'] = user_username
    yield payload
