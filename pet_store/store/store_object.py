from pet_store.base_object import BaseObject
from utils.request import APIRequest
from config import *


class StoreObject(BaseObject):

    def __init__(self):
        super().__init__()
        self.request = APIRequest()

    def get_pet_inventory(self):
        return self.request.get(STORE_INVENTORY_URL)


