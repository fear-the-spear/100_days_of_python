import requests

URL = "https://api.sunrise-sunset.org/json"
MY_LAT = "40.869331"
MY_LNG = "-82.317917"

params = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}
response = requests.get(URL, params=params)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise, sunset)
