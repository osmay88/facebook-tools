import click
from utils import store_credentials
from get_page_token import get_page_access_token


@click.group()
def cli():
    pass

@click.command()
def creds():
    app_id = input("Facebook app_id: ")
    app_secret = input("Facebook app_secret: ")
    click.echo("Storing facebook credentiasl")
    store_credentials(app_id, app_secret)


@click.command()
def pagetoken():
    user_long_lived_token = input("User long lived access token: ")
    user_id = input("Facebook user id: ")
    data = get_page_access_token(user_long_lived_token, user_id)
    for page in data.get('data'):
        click.echo(f"Page name:{page.get('name')} Access_token: {page.get('access_token')}")
        click.echo("")



cli.add_command(creds)
cli.add_command(pagetoken)

if __name__ == '__main__':
    cli()