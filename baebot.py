'''
Created by Charlie, Ammar, Leila, Teddy
This is the source code for our chatbot BaeBot
'''

import nltk

#Tokenizes the response given by the user.
def tokenize(response):
	tokens = nltk.word_tokenize(response)
	tagged = nltk.pos_tag(tokens)
	print tagged #TEMPORARY, should return tagged


#main function, provides loop that allows for the back and forth between BaeBot and the conversation
def main():
	print "hey bb, hows it going?"
	convoComplete = True
	while(convoComplete): #loop until conversation is satisfied
		baeBotResponse = "sup"
		n = raw_input(baeBotResponse + "\n") # prints Baebot question, takes input from user
		if (n == 'not much'): # TEMPORARY, should evaluate response
			convoComplete = False
			tokenize(n)
		


#Initiate convo
main()
