import json

# Data to be written to a JSON file
data = [
    {
        "id": 1,
        "first_name": "Anne",
        "last_name": "Kokkoniemi",
        "email": "annek@gmail.com",
        "gender": "Female",
        "ip_address": "",
        "country_code": "FI"
    },
    {
        "id": 2,
        "first_name": "Claudia",
        "last_name": "Jimon",
        "email": "claudia@gmail.com",
        "gender": "Female",
        "ip_address": "",
        "country_code": "RO"
    },
    {
        "id": 3,
        "first_name": "Marcin",
        "last_name": "Szesniak",
        "email": "marcin@gmail.com",
        "gender": "Male",
        "ip_address": "",
        "country_code": "PO"
    },
    {
        "id": 4,
        "first_name": "Anne",
        "last_name": "Kinsey",
        "email": "annek@gmail.com",
        "gender": "Female",
        "ip_address": "",
        "country_code": "US"
    }
]

# Write the data to a JSON file
with open('data.json', 'w') as file:
    json.dump(data, file)
