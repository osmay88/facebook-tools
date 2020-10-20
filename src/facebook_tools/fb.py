import click
from cred_utils import store_credentials
from token_utils import get_page_access_token, get_user_long_lived_token, debug_access_token
from messaging import send_text_dm
from commands import(
                        creds,
                        pagetoken,
                        userlonglived,
                        sendtext,
                        debugtoken
                    )


@click.group()
def cli():
    pass


cli.add_command(creds)
cli.add_command(pagetoken)
cli.add_command(userlonglived)
cli.add_command(sendtext)
cli.add_command(debugtoken)

if __name__ == '__main__':
    cli()