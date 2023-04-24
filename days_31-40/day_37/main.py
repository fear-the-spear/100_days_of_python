import requests
from datetime import datetime
from PRIVATE.variables import *
pixela_endpoint = "https://pixe.la/v1/users"

# STEP 1. Create User
# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# STEP 2.
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# graph_config = {
#     "id": GRAPH_ID,
#     "name": GRAPH_NAME,
#     "unit": "line",
#     "type": "int",
#     "color": "ajisai"
# }

# passing the token in the header hides the token from hack artists
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(
#     url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# STEP 3. Get the Graph!
# go to: https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}.html

# STEP 4. Post a Pixel
pixela_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# today = datetime(year=2023, month=4, day=21)
# qty = "100"

# pixela_data = {
#     "date": today.strftime("%Y%m%d"),
#     "quantity": qty
# }

# response = requests.post(
#     url=pixela_creation_endpoint, json=pixela_data, headers=headers)
# print(response.text)

# print(today)

# STEP 5. Update a current pixel

# pixela_data = {
#     "quantity": "85",
# }

# response = requests.put(
#     url=f"{pixela_creation_endpoint}/20230423",
#     json=pixela_data,
#     headers=headers
# )

# print(response.text)

# STEP 6. Delete a current pixel
response = requests.delete(
    url=f"{pixela_creation_endpoint}/20230422", headers=headers)
print(response.text)
