import click
from utils import store_credentials
from token_utils import get_page_access_token, get_user_long_lived_token


@click.group()
def cli():
    pass

@click.command(help="Store the app credentials locally")
def creds():
    app_id = click.prompt("Facebook app_id: ")
    app_secret = click.prompt("Facebook app_secret: ")
    click.echo("Storing facebook credentiasl")
    store_credentials(app_id, app_secret)


@click.command(help="Get a user long lived access token.")
def userlonglived():
    user_token = click.prompt("Facebook user token: ")
    data = get_user_long_lived_token(user_token)
    click.echo(f"User long lived token: {data}")


@click.command(help="Get a page long lived token from.")
def pagetoken():
    user_long_lived_token = click.prompt("User long lived access token: ")
    user_id = click.prompt("Facebook user id: ")
    data = get_page_access_token(user_long_lived_token, user_id)
    for page in data.get('data'):
        click.echo("")
        click.echo(f"Page name:{page.get('name')} Access_token: {page.get('access_token')}")
        click.echo("")



cli.add_command(creds)
cli.add_command(pagetoken)
cli.add_command(userlonglived)

if __name__ == '__main__':
    cli()