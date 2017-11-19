# FlirtBot
Created by Charlie, Ammar, Leila, Teddy

This is a bot that is meant to seduce you, prepare yourselves.

How to run our bot:
Open terminal, cd into the folder that contains this project, and run the command:

python baebot.py

----------------------------------------------------------------------------------
List of libraries used:
NLTK
ast
pickle
vaderSentiment
random

----------------------------------------------------------------------------------
FlirtBot seq2seq model:

Dependencies
============
* numpy
* scipy 
* six
* tensorflow (https://www.tensorflow.org/versions/r0.12/get_started/os_setup.html) -- USE tensorflow 0.12

Use [pip](https://pypi.python.org/pypi/pip) to install any missing dependencies


Usage
===========

To train the bot, edit the `seq2seq.ini` file so that mode is set to train like so

`mode = train`

then run the code like so

``python execute.py``

To test the bot during or after training, edit the `seq2seq.ini` file so that mode is set to test like so

`mode = test`

then run the code like so

``python execute.py``
