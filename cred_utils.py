import json
from os.path import expanduser


HOME = expanduser("~")

def store_credentials(app_id: str, app_secret: str):
    with open(f"{HOME}/.fb", "w+") as file:
        data = {
            "app_id": app_id,
            "app_secret": app_secret 
        }
        file.writelines(json.dumps(data, indent=4))
    

def get_credentials():
    with open(f"{HOME}/.fb", "r+") as file:
        data = "".join(file.readlines())
        return json.loads(data)
