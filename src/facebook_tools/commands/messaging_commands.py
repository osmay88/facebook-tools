import json
import click
from facebook_tools.messaging import send_text_dm, get_conversations
from facebook_tools.utils import launch_editor

MESSAGE_TYPE = ("text", "quickreply", "postback")
TYPE_HELP = """Select the message type to be send. Options: %s""" % ", ".join(MESSAGE_TYPE)


@click.command(help="Send a text direct message")
@click.option("-i", "--interactive", is_flag=True, flag_value=False, help="Ask for parameters for filling the message")
@click.option("-t", "--type", type=str , help=TYPE_HELP)
@click.option("-a", "--token", type=str, default=None, help="Facebook access token")
def sendmessage(interactive, type, token):
    if not type or type not in MESSAGE_TYPE:
        click.echo("Type is missing or invalid type. Got %s" % type)

    if not token:
        token = click.prompt("Page access token: ")

    user_id = None
    text = None
    if interactive:
        user_id = click.prompt("Recipient ID: ")
        text = click.prompt("Text: ")
    if type == "text":
        result = send_text_dm(user_id, text, token)
        click.echo(result)
    else:
        click.echo("Not implemented yet.")


@click.command(help="Get a list of conversations for a page")
def getconversations():
    access_token = click.prompt("Page access token: ")
    conversations = get_conversations(access_token)
    conversations = conversations.get("conversations").get("data")
    click.echo(json.dumps(conversations, indent=2))

@click.command(help="Get the list of messages for a converstion")
@click.option("--fields", default="", type=str, help="Use FB grahp syntax to select conversation fields")
def getmessages(fields):
    data = launch_editor("hello world")
    click.echo(data)