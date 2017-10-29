'''
Created by Charlie, Ammar, Leila, Teddy
This is the source code for our chatbot BaeBot
'''

import nltk
import random
#import narrativeStuff



#Tokenizes the response given by the user.
def tokenize(response):
	tokens = nltk.word_tokenize(response)
	tagged = nltk.pos_tag(tokens)
	print tagged #TEMPORARY, should return tagged


def pickOpener():
	openerNum = random.randint(1,4)
	return #some sentence FIXIT

def makeFlirt(response, convoComplete, flirtyWeight):
	'''
	1. Tag response ... tokenize
	2. Sentiment analysis http://www.nltk.org/howto/sentiment.html does it help???
	3. amI... 
	3.5. based on sentiment and keywords, look for response in response dict, return that
	'''

def amIDealingWithADickhead(flirtyWeight):
	#if a dickhead, end convo
	#else: keep going

#main function, provides loop that allows for the back and forth between BaeBot and the conversation
def main():
	convoComplete = True
	flirtyWeight = 0
	baeBotResponse = pickOpener()
	while(convoComplete): #loop until conversation is satisfied
		response = raw_input(baeBotResponse + "\n") # prints Baebot question, takes input from user
		baeBotResponse = makeFlirt(response)





#Initiate convo
tokenize("My Name is Ammar.")
