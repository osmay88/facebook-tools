import click
from base import execute_facebook_request
from token_utils import debug_access_token


def send_text_dm(to, text_message, access_token):
    _endpoint = "/me/messages"
    payload = {
        "messaging_type": "RESPONSE",
        "recipient": {
            "id": to
            },
            "message": {
                "text": text_message
        }   
    }

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
    

