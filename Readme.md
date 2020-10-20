## Utility for handling Facebook stuff

# How to install:
- From the root folder run `./install` this will create a virtual environment and install the requirements.
- Update your `$PATH` to include this folder. Remember to reload you bash env.
- Run `fb creds` to set your applications credentials. Right now it only support one active FB app. Working on get suppor for simultaneous apps.
- run `fb --help` to get the current active commands

# Supported commands:
- `creds` store the facebook app credentials locally 
- `pagetoken` get a long lived token for a page
- `userloglived` get a user long lived token from a regular token
- more stuff will come soon ...
