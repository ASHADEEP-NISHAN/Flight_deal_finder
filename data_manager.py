import requests
import os
from pprint import pprint
SHEETY_PRICES_ENDPOINT="https://api.sheety.co/ef4a2d58feee89465b92b29f46ee213b/flightDeals/prices"
SHEETY_USERS_ENDPOINT="https://api.sheety.co/ef4a2d58feee89465b92b29f46ee213b/flightDeals/users"
# Bearer="hfnourneliuh9hgrenIUGNFONI"
Bearer=os.environ.get("Bearer")
headers = {
            "Authorization": f"Bearer {Bearer}"}
class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):

        response = requests.get(url=SHEETY_PRICES_ENDPOINT,headers=headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_customers_emails(self):
        response=requests.get(url=SHEETY_USERS_ENDPOINT)
        data=response.json()
        self.customer_data = data["users"]
        return self.customer_data
