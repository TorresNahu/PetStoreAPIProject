from json import dumps

from config import *
from utils.request import APIRequest


class BasePet:
    def __init__(self):
        self.request = APIRequest()

        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

    def add_new_pet_to_the_store(self, body=None):
        pet_id, response = self.__create_new_unique_pet(body)
        return pet_id, response

    def __create_new_unique_pet(self, body):
        unique_pet_id = body['id']
        payload = dumps(body)
        response = self.request.post(BASE_URL, payload, self.headers)
        return unique_pet_id, response

    def update_existing_pet(self, body):
        pass

    def get_pet_by_id(self, pet_id):
        return self.request.get(f'{BASE_URL_PET}{pet_id}')

    def get_pets_by_status(self, status):
        """
        :param status: Str. Available values: available, pending, sold
        :return: All pets with the provided status.
        """
        return self.request.get(f'{FIND_PET_BY_STATUS_URL}{status}')

    def delete_a_pet(self, pet_id):
        pass

    def search_pets_by_condition(self, pets, pet_expected, condition):
        pet_names_list = []
        for pet in pets:
            if pet[condition] == pet_expected:
                pet_names_list.append(pet)
                break

        return pet_names_list
