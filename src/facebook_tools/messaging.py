import click
import json
from base import execute_facebook_request
from token_utils import debug_access_token
from facebook_tools.utils import launch_editor
from facebook_tools.payloads import TEXT_MESSAGE


def send_text_dm(to, text_message, access_token):
    _endpoint = "/me/messages"
    if to and text_message:
        TEXT_MESSAGE["recipient"]["id"] = id
        TEXT_MESSAGE["message"]["text"] = text_message
    else:
        payload_str = launch_editor(json.dumps(TEXT_MESSAGE, indent=2))
        payload = json.loads(payload_str)

    params = {
        "access_token": access_token
    }
    return execute_facebook_request("post", _endpoint, payload=payload, params=params).json()

def get_conversations(access_token):
    token_data = debug_access_token(access_token).get("data")
    # click.echo(token_data)
    page_id = token_data.get("profile_id")
    if not page_id:
        click.echo("Cannot extract page information from token")
        return
    _endpoint = "/%s/?fields=conversations{id, senders}" % page_id
    params = {
        "access_token": access_token
    }
    return execute_facebook_request("get", _endpoint, None, params=params).json()
    

