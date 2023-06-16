import requests
from pprint import pprint
AUTH_TOKEN = "cHlsb3Q6c29mdHdvcng="
SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/d51e2670e5420f10ef9236278431d7c0/flightDeals/prices"


class DataManager:
    def __init__(self):
        self.headers = {"Content-Type": "application/json",
                        "Authorization": f"Basic ${AUTH_TOKEN}"}
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(
            url=SHEETY_PRICES_ENDPOINT, headers=self.headers)
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
                headers=self.headers,
                json=new_data
            )
            print(response.text)
