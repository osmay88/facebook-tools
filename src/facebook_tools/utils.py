import sys, tempfile, os
from subprocess import call


def launch_editor(prefill_text:str):
    EDITOR = os.environ.get('EDITOR','vim') #that easy!

    initial_message = b"hello world" # if you want to set up the file somehow

    with tempfile.NamedTemporaryFile(suffix=".tmp") as tf:
        tf.write(prefill_text.encode())
        tf.flush()
        call([EDITOR, '+set backupcopy=yes', tf.name])
        tf.seek(0)
        edited_message = tf.read()
        return edited_message.decode()