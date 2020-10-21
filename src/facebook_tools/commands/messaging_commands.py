import json
import click
from facebook_tools.messaging import send_text_dm, get_conversations


@click.command(help="Send a text direct message")
def sendtext():
    user_id = click.prompt("Recipient ID: ")
    text = click.prompt("Text: ")
    access_token = click.prompt("Page access token: ")
    result = send_text_dm(user_id, text, access_token)
    click.echo(result)


@click.command(help="Get a list of conversations for a page")
def getconversations():
    access_token = click.prompt("Page access token: ")
    conversations = get_conversations(access_token)
    conversations = conversations.get("conversations").get("data")
    click.echo(json.dumps(conversations, indent=2))

@click.command(help="Get the list of messages for a converstion")
@click.option("--fields", default="", type=str, help="Use FB grahp syntax to select conversation fields")
def getmessages(fields):
    click.echo(fields)