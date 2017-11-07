'''
Created by Charlie, Ammar, Leila, Teddy
This is the source code for our chatbot BaeBot
'''

import nltk
from nltk.tokenize import word_tokenize
import random
import ast
import pickle
import NarrativeTreeStructure
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer




#Tokenizes the response given by the user.
def tokenize(response):
	tokens = nltk.word_tokenize(response)
	tagged = nltk.pos_tag(tokens)
	print tagged #TEMPORARY, should return tagged


def pickOpener():
	openerNum = random.randint(0,2)
	if openerNum == 0:
		Opening = "Hey baby, come here often?"
	elif openerNum == 1:
		Opening = "Hey there hot stuff, whatchya doin tonight?"
	else:
		Opening = "Hey lover, whats going on?"
	return Opening

def makeFlirt(response, convoComplete, flirtyWeight):
	'''
	1. Tag response ... tokenize
	2. Sentiment analysis http://www.nltk.org/howto/sentiment.html does it help???
	3. amI... 
	3.5. based on sentiment and keywords, look for response in response dict, return that
	'''

#def amIDealingWithADickhead(flirtyWeight):
	#if a dickhead, end convo
	#else: keep going

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


def nextNode(storyTree, curNode, flirtiness):

	if flirtiness['compound'] >= 0:
		for node in storyTree:
			if node.name == curNode.positiveLink:
				return node
	else:
		for node in storyTree:
			if node.name == curNode.negativeLink:
				return node

def updateFlirtyWeight(flirtiness, currentWeight):
	print flirtiness
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
	#result = analyze("You are beautiful!", classifier, dictionary)


	convoComplete = True
	flirtyWeight = 0
	baeBotResponse = pickOpener()
	storyTree = NarrativeTreeStructure.assignStructure()
	curNode = "Start"
	flirtyWeight = 0
	analyzer = SentimentIntensityAnalyzer()

	
	while(convoComplete): #loop until conversation is satisfied

		response = raw_input(baeBotResponse + "\n") # prints Baebot question, takes input from user
		
		if curNode == "Start":
			curNode = storyTree[len(storyTree) -1]
		else:
			curNode = nextNode(storyTree, curNode, analyzer.polarity_scores(response))

		if curNode == None:
			print flirtyWeight
			break
		baeBotResponse = curNode.sentence
		flirtyWeight = updateFlirtyWeight(analyze(response, classifier, dictionary), flirtyWeight)

		








if __name__ == "__main__":
	main()


##Initiate convo
#tokenize("My Name is Ammar.")