'''
Created by Charlie, Ammar, Leila, Teddy
This is the source code for our chatbot BaeBot
'''

import nltk
from nltk.tokenize import word_tokenize

import ast
import pickle
import NarrativeTreeStructure
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer




#Tokenizes the response given by the user.
def tokenize(response):
	tokens = nltk.word_tokenize(response)
	tagged = nltk.pos_tag(tokens)
	print tagged #TEMPORARY, should return tagged
	

def analyze(sentence, classifier, dictionary):
	sentence_features = {word.lower(): (word in word_tokenize(sentence.lower())) for word in dictionary}
	return classifier.classify(sentence_features)

def getClassifier():
	training_data_file = "training_data.txt"
	dictionary_file = "dictionary.txt"
	training_data = open(training_data_file,"r")
	dictionary_data = open(dictionary_file,"r")
	data = training_data.readline()
	dictionary_string = dictionary_data.readline()
	dictionary = ast.literal_eval(dictionary_string)
	training_data_list = ast.literal_eval(data)
	classifier = nltk.NaiveBayesClassifier.train(training_data_list)
	with open('classifier.txt', 'wb') as classifier_file:
		pickle.dump(classifier, classifier_file)
	with open('dict.txt', 'wb') as dict_file:
		pickle.dump(dictionary, dict_file)


#Goes to the next node in the story tree, based on positive/negative response
def nextNode(storyTree, curNode, flirtiness):

	if flirtiness >= 0:
		for node in storyTree:
			if node.name == curNode.positiveLink:
				return node
	else:
		for node in storyTree:
			if node.name == curNode.negativeLink:
				return node

#increments the flirty weight based on the response
def updateFlirtyWeight(flirtiness, currentWeight):
	
	if flirtiness == "flirty":
		currentWeight += .1
	else:
		currentWeight -=.1

	return currentWeight




#main function, provides loop that allows for the back and forth between BaeBot and the conversation
def main():
	with open('classifier.txt', 'rb') as classifier_file:
		classifier = pickle.load(classifier_file)
	with open('dict.txt', 'rb') as dict_file:
		dictionary = pickle.load(dict_file)
<<<<<<< HEAD
	result = analyze("Good.", classifier, dictionary)
	print result
	result2 = analyze("Bad.", classifier, dictionary)
	print result2
#	convoComplete = True
#	flirtyWeight = 0
#	baeBotResponse = pickOpener()
#	while(convoComplete): #loop until conversation is satisfied
#		response = raw_input(baeBotResponse + "\n") # prints Baebot question, takes input from user
#		baeBotResponse = makeFlirt(response)
=======
	#result = analyze("You are beautiful!", classifier, dictionary)


	convoComplete = True
	flirtyWeight = 0
	storyTree = NarrativeTreeStructure.assignStructure()
	curNode = "Start"
	flirtyWeight = 0
	analyzer = SentimentIntensityAnalyzer()

	
	while(convoComplete): #loop until conversation is satisfied	
		if curNode == "Start":
			curNode = storyTree[len(storyTree) -1]

		elif curNode.name == 'decision':
			if flirtyWeight > 0:
				curNode = nextNode(storyTree, curNode, 1)
			else:
				curNode = nextNode(storyTree, curNode, -1)
		else:
			curNode = nextNode(storyTree, curNode, analyzer.polarity_scores(response)['compound'])

		if curNode == None:
			print "The bot has left the chat!"
			break

		baeBotResponse = curNode.sentence

		response = raw_input(baeBotResponse + "\n") # prints Baebot question, takes input from user
		flirtyWeight = updateFlirtyWeight(analyze(response, classifier, dictionary), flirtyWeight)
		







>>>>>>> bea1799b56d3e3123200252c6afceff2b156629c

if __name__ == "__main__":
	main()


##Initiate convo
#tokenize("My Name is Ammar.")