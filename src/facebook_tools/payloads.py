

TEXT_MESSAGE = {
    "messaging_type": "RESPONSE",
    "recipient": {
        "id": "<PSID>"
    },
    "message": {
        "text": "<MESSAGE TEXT>"
    }
}

QUICK_REPLY = {
    "recipient": {
        "id": "<PSID>"
    },
    "messaging_type": "RESPONSE",
    "message": {
        "text": "Pick a color:",
        "quick_replies": [
            {
                "content_type": "text",
                "title": "Red",
                "payload": "<POSTBACK_PAYLOAD>",
                "image_url": "http://example.com/img/red.png"
            }, {
                "content_type": "text",
                "title": "Green",
                "payload": "<POSTBACK_PAYLOAD>",
                "image_url": "http://example.com/img/green.png"
            }
        ]
    }
}


POSTBACK = {
    "recipient": {
        "id": "<PSID>"
    },
    "message": {
        "attachment": {
            "type": "template",
            "payload": {
                "template_type": "button",
                "text": "Try the postback button!",
                "buttons": [
                    {
                        "type": "postback",
                        "title": "Postback Button",
                        "payload": "DEVELOPER_DEFINED_PAYLOAD"
                    }
                ]
            }
        }
    }
}
