#!/bin/bash


DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

echo "Creating python virtual enviroment"
python3 -m venv venv

echo "Installing requirements"
source $DIR/venv/bin/activate
pip install -r $DIR/requirements.txt

python setup.py install

echo 'Updating BASH path'
echo 'export PATH=$PATH:$DIR'>>$HOME/.bash_profile

# echo "Adding folder to PATH"
# if [$SHELL = "/bin/bash"] || [$SHELL = "/bin/sh"]
# then
#     echo 'Updating BASH path'
#     echo 'export PATH=$PATH:$DIR'>>$HOME/.bash_profile
# elif $SHELL = "/bin/zsh"
# then
#     echo 'Updating ZSH path'
#     echo 'export PATH=$PATH:$DIR'>>$HOME/.zshrc
# fi

echo "All done."

