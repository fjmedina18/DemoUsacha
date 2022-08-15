import requests
import json


def get_token():
    url = "https://devnetsandbox.cisco.com/api/aaalogin.json"

    payload = {
        "aaaUser": {
            "attributes": {
                "name": "admin",
                "pwd": "!v3G@!4@Y"
            }
        }
    }
