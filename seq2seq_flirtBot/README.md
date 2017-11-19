# Tensorflow Chatbot

DISCLAIMER: MOST OF THE CODE IS TAKEN FROM A PUBLIC GIT REPOSITORY FOR MAKING SEQ2SEQ CHATBOTS
(https://github.com/llSourcell/tensorflow_chatbot)

Dependencies
============
* numpy
* scipy 
* six
* tensorflow (https://www.tensorflow.org/versions/r0.12/get_started/os_setup.html) -- USE tensorflow 0.12

Use [pip](https://pypi.python.org/pypi/pip) to install any missing dependencies

Data Preparation
================
Go to the directory data/dataDir and run: python dataCleaner.py and copy the train and test files to ../

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

Credits
===========
Credit for the vast majority of code here goes to [suriyadeepan](https://github.com/suriyadeepan) and @Sirajology.
All we did was clean up the data for our corpus and train the given model on it.