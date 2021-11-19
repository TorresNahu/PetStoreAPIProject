from json import dumps

from pet_store.base_object import BaseObject
from utils.request import APIRequest
from config import *


class UserObject(BaseObject):
    def __init__(self):
        super().__init__()
        self.request = APIRequest()

    def create_user(self, body):
        username, response = self.__create_new_user(body)
        return username, response
    
    def __create_new_user(self, body):
        username = body['username']
        payload = dumps(body)
        response = self.request.post(BASE_USER_URL, payload, headers=self.headers)
        return username, response

    def get_user_by_username(self, username):
        return self.request.get(f'{BASE_USER_URL}/{username}')

    def delete_user(self, username):
        return self.request.delete(f'{BASE_USER_URL}/{username}')

    def login_user_into_the_system(self, username, password):
        url = f'{LOGIN_URL}?username={username}&password={password}'
        return self.request.get(url)

    def logout_user_into_the_system(self):
        return self.request.get(LOGOUT_URL)
