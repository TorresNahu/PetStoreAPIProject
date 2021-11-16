import pytest
from uuid import uuid4
from utils.file_reader import read_file


@pytest.fixture
def create_pet_data():
    payload = read_file('create_pet.json')
    unique_pet_id = str(uuid4())
    unique_pet_name = f'Pet {unique_pet_id}'

    payload['id'] = unique_pet_id
    payload['name'] = unique_pet_name
    yield payload
