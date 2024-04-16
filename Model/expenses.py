import json
import requests

from .users import User
from .category import Category
from .constants import SERVER_URL

class Expense:
    ENDPOINT = "/expenses/"

    def __init__(self, user = None,category = None, exp_name=None, description=None, amount=None, id=None, **kwargs) -> None:
        self.id = id
        self.user = user
        self.category = category
        self.exp_name =  exp_name
        self.description = description
        self.amount = amount
        

        if isinstance(user, dict):
            self.user = User(**user)
        else:
            self.user = user

    def save(self):
        url = f"{SERVER_URL}{self.ENDPOINT}"

        payload = {'user': self.user,
        'category': self.category,
        'exp_name': self.exp_name,
        'dexcription': self.description,
        'amount': self.amount}
        
        headers = {}

        if not self.id:
            response = requests.request("POST", url, headers=headers, data=payload)

            data = json.loads(response.text)
            self.id = data['id']
        else:
            url += str(self.id)
            response = requests.request("PATCH", url, headers=headers, data=payload)

    def read(id=None):
        url = f"{SERVER_URL}{__class__.ENDPOINT}"
        url += id if id else ''

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        response:dict = json.loads(response.text)

        if id:
            expense = __class__(**response)
            return expense
        else:
            expenses = []

            for result in response:
                expense = __class__(**result)
                expenses.append(expense)
        
            return expenses

    def delete(self):
        url = f"{SERVER_URL}{self.ENDPOINT}{self.id}"

        payload, headers = {}, {}

        response = requests.request("DELETE", url, headers=headers, data=payload)

        try:
            response.raise_for_status()

            self.id = None
        except Exception as e:
            raise e
        
    def toJSON(self):
        dictionary = {
            "id": self.id,
            "user": self.user,
            "category": self.category,
            "exp_name": self.exp_name,
            "description": self.description,
            "amount": self.amount
        }

        return dictionary