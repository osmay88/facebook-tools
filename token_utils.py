#!/usr/bin/python3.8
import json
import requests
from urllib.parse import urljoin
from cred_utils import get_credentials


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


def get_user_long_lived_token(user_token: str):
    fb_credentials = get_credentials()
    params = {
        "grant_type": "fb_exchange_token",
        "client_id": fb_credentials.get("app_id"),
        "client_secret": fb_credentials.get("app_secret"),
        "fb_exchange_token": user_token
    }
    return execute_facebook_request("get", endpoint="/oauth/access_token", params=params).json()


def get_page_access_token(user_long_lived_token: str, user_id: str):
    params = {
        "access_token": user_long_lived_token
    }
    return execute_facebook_request("get", endpoint=f"/{user_id}/accounts", params=params).json()
