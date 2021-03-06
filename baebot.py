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




#Tokenizes the response given by the user, collects specific parts of speech depending on input
def getProperNoun(response, infoType):
	info = ""
	tokens = nltk.word_tokenize(response)
	tagged = nltk.pos_tag(tokens)

	if infoType == 'name' or infoType == 'shirtLocation':
		for element in tagged:
			if element[1] == "NNP":
				if info == '':
					info = element[0]
				else:
					info = info + " " + element[0]

	if infoType == 'occupation':
		for element in tagged:
			if element[1] == "NN":
				if info == '':
					info = element[0]
				else:
					info = info + " " + element[0]

	if infoType == 'foodType':
		for element in tagged:
			if element[1] == "JJ":
				if info == '':
					info = element[0]
				else:
					info = info + " " + element[0]


	return info
	
#tokenizes elements of sentence and uses our already made flirty classifier and our dictionary of words to classify the sentence as flirty or not
def analyze(sentence, classifier, dictionary):
	sentence_features = {word.lower(): (word in word_tokenize(sentence.lower())) for word in dictionary}
	return classifier.classify(sentence_features)

#Accesses training data and dictionary files, which are strings, and places them in new files using pickle, so that they can be accessed without having to convert their data structure. Note this only needs to be run after running sentiment_analysis.py
def getClassifier():
	training_data_file = "training_data.txt"
	dictionary_file = "dictionary.txt"
	training_data = open(training_data_file,"r")
	dictionary_data = open(dictionary_file,"r")
	data = training_data.readline()
	dictionary_string = dictionary_data.readline()
	print dictionary_string
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

#checks for special cases such as swearing or 'your mom' and exits the conversation if it finds something 
def specialCases(inp):
	swears = ['anal','anus','arse','ass','ballsack','balls','bastard','bitch','biatch','blowjob','blow job','bollock','bollok','boner','boob','bugger','bum','butt','buttplug','cock','cunt','damn','dick','dildo','dyke','fag','feck','fellate','fellatio','felching','fuck','f u c k','goddamn','god damn','hell','homo','jerk','jizz','nigger','nigga','penis','piss','poop','prick','pube','pussy','scrotum','slut','smegma','twat','wank','whore','wtf']
	for word in inp.split():
		plural = word + 's'
		if word in swears or plural in swears:
			print  "Um...I don't appreciate your language rn."
			print "The bot has left the conversation!"
			exit(0)


	if 'talk dirty' in inp or 'dirty talk' in inp or 'dirty talking' in inp or 'talking dirty' in inp:
		print "Hey! I'm not that kind of bot!"
		print "The bot has left the conversation!"
		exit(0)

	elif 'your mom' in inp or 'ur mom' in inp:
		print "VERY mature :P I'm just trying to have a pleasant conversation ugh"
		print "The bot has left the conversation!"
		exit(0)

	elif 'fav' in inp and 'prof' in inp:
		print "Blake Howald is hands down the coolest professor ever, so cool in fact that I must leave rn."
		print "The bot has left the conversation!"
		exit(0)

	else:
		return None


#This function controls the collection of information during the first phase of the narrative
def captureInfo(curNode, response):

	info = ''

	if curNode.name == 'p1R1':
		info = getProperNoun(response, 'shirtLocation')
	if curNode.name == 'p1R2':
		info = getProperNoun(response, 'foodType')
		
	if curNode.name == 'p1R3':
		info = getProperNoun(response, 'name')
	if curNode.name == 'p1R4':
		info = getProperNoun(response, 'occupation')
		
	return info


#main function, provides loop that allows for the back and forth between BaeBot and the conversation
def main():
#	getClassifier()
	with open('classifier.txt', 'rb') as classifier_file:
		classifier = pickle.load(classifier_file)
	with open('dict.txt', 'rb') as dict_file:
		dictionary = pickle.load(dict_file)

	convoComplete = True
	flirtyWeight = 0
	storyTree = NarrativeTreeStructure.assignStructure()
	curNode = "Start"
	flirtyWeight = 0
	analyzer = SentimentIntensityAnalyzer()
	capturedInfo = ''

	
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
		baeBotResponse = baeBotResponse.replace(';]', capturedInfo)

		response = raw_input(baeBotResponse + "\n") # prints Baebot question, takes input from user
		capturedInfo = captureInfo(curNode, response)
		extra = specialCases(response)
		if extra is not None: print extra
		flirtyWeight = updateFlirtyWeight(analyze(response, classifier, dictionary), flirtyWeight)
		

if __name__ == "__main__":
	main()
