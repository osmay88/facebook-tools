#!/usr/bin/python3.8
import json
import requests
from urllib.parse import urljoin
from cred_utils import get_credentials
from base import execute_facebook_request


def get_user_long_lived_token(user_token: str):
    fb_credentials = get_credentials()
    params = {
        "grant_type": "fb_exchange_token",
        "client_id": fb_credentials.get("app_id"),
        "client_secret": fb_credentials.get("app_secret"),
        "fb_exchange_token": user_token
    }
    return execute_facebook_request("get", endpoint="/oauth/access_token", params=params).json()


def get_page_access_token(user_long_lived_token: str, user_id: str = None):
    params = {
        "access_token": user_long_lived_token
    }
    token_data = debug_access_token(user_long_lived_token)
    _user_id = token_data.get('data').get("user_id")
    return execute_facebook_request("get", endpoint=f"/{_user_id}/accounts", params=params).json()


def debug_access_token(access_token):
    _endpoint = "/debug_token"
    params = {
        "access_token": access_token,
        "input_token": access_token
    }
    return execute_facebook_request("get", _endpoint, None, params).json()


def authenticate_page(user_token, app_id):
    pass
