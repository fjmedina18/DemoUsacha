import requests
import json


def get_token():
    url = "https://10.10.20.14/api/aaalogin.json"

    payload = {
        "aaaUser": {
            "attributes": {
                "name": "admin",
                "pwd": "Cisco12345"
            }
        }
    }
