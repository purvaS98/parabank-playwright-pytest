import json


def get_credentials():
    with open("test_data/config.json", "r") as file:
        config = json.load(file)

    return config["username"], config["password"]