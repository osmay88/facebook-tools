import requests
from urllib.parse import urljoin


FACEBOOK_API = "https://graph.facebook.com"
FACEBOOK_API_VERSION = "v8.0"


def execute_facebook_request(method: str, endpoint:str, payload=None, params=None):
    """
    """
    _endpoint = endpoint if endpoint.startswith("/") else f"/{endpoint}"
    _url = urljoin(FACEBOOK_API, FACEBOOK_API_VERSION+endpoint)
    result = None
    if method == "post":
        result = requests.post(_url, json=payload, params=params)
    elif method == "get":
        result = requests.get(_url, params=params)

    result.raise_for_status()
    return result