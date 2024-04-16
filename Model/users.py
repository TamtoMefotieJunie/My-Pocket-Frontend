import os
import sqlite3
import json
import requests

from .constants import SERVER_URL

class User:
    ENDPOINT = "/users/"

    def __init__(self, id=None, name=None, email=None, password=None) -> None:
        self.id = id
        self.name = name
        self.email = email
        self.password = password

    def save(self):
        url = f"{SERVER_URL}{self.ENDPOINT}"

        payload = {'name': self.name,'email' : self.email,'password' : self.password}
        headers = {}

        if not self.id: # save to the backend with a POST request
            response = requests.request("POST", url, headers=headers, data=payload)

            data = json.loads(response.text)
            self.id = data['id']
        else: # update a particular subject
            url += str(self.id)
            response = requests.request("PATCH", url, headers=headers, data=payload)


    def read(id=None):
        url = f"{SERVER_URL}{__class__.ENDPOINT}"
        url += id if id else ''

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        response = json.loads(response.text)

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