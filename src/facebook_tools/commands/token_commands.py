import click
import json
from facebook_tools import token_utils
from facebook_tools.token_utils import (get_page_access_token, get_user_long_lived_token, debug_access_token)
from facebook_tools.cred_utils import store_credentials, get_credentials
from facebook_tools.messaging import send_text_dm


@click.command(help="Store the app credentials locally")
@click.option("-v", "--view", is_flag=True, flag_value=True, help="Display current credentials")
def creds(view):
    if not view:
        app_id = click.prompt("Facebook app_id: ")
        app_secret = click.prompt("Facebook app_secret: ")
        click.echo("Storing facebook credentiasl")
        store_credentials(app_id, app_secret)
    else:
        creds = get_credentials()
        click.echo(json.dumps(creds, indent=2))


@click.command(help="Get a user long lived access token.")
def userlonglived():
    user_token = click.prompt("Facebook user token: ")
    data = get_user_long_lived_token(user_token)
    click.echo(f"User long lived token: {data}")


@click.command(help="Get a page long lived token.")
def pagetoken():
    user_long_lived_token = click.prompt("User long lived access token: ")
    # user_id = click.prompt("Facebook user id(type 0 to ignore): ", default=None)
    data = get_page_access_token(user_long_lived_token, None)
    for page in data.get('data'):
        click.echo("")
        click.echo(f"Page name:{page.get('name')} Access_token: {page.get('access_token')}")
        click.echo("")

@click.command(help="Send a text direct message")
def sendtext():
    user_id = click.prompt("Recipient ID: ")
    text = click.prompt("Text: ")
    access_token = click.prompt("Page access token: ")
    result = send_text_dm(user_id, text, access_token)
    click.echo(result)


@click.command()
def debugtoken():
    access_token = click.prompt("facebook access token: ")
    result = debug_access_token(access_token)
    click.echo(json.dumps(result, indent=2))