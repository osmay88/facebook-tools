from base import execute_facebook_request


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
    
    return execute_facebook_request("post", _endpoint, payload=payload, params=params)