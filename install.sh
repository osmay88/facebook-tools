#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

echo "Creating virtual enviroment"
python3 -m venv venv

source venv/bin/activate
pip install -r requirements.txt

echo "Adding folder to PATH"
if [$0 = "bash"] || [$0 = "sh"]
then
    echo 'export PATH=$PATH:$DIR'>>$HOME/.bash_profile
elif $0 = "zsh"
then
    echo 'Updating ZSH path folder'
    # TODO
fi

