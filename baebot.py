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

#checks for special cases 
def specialCases(inp):
	swears = ['anal','anus','arse','ass','ballsack','balls','bastard','bitch','biatch','blowjob','blow job','bollock','bollok','boner','boob','bugger','bum','butt','buttplug','cock','cunt','damn','dick','dildo','dyke','fag','feck','fellate','fellatio','felching','fuck','f u c k','goddamn','god damn','hell','homo','jerk','jizz','nigger','nigga','penis','piss','poop','prick','pube','pussy','scrotum','slut','smegma','twat','wank','whore','wtf']
	for word in inp.split():
		plural = word + 's'
		if word in swears or plural in swears:
			return "Um...I don't appreciate your language rn."

	if 'talk dirty' in inp or 'dirty talk' in inp or 'dirty talking' in inp or 'talking dirty' in inp:
		return "Hey! I'm not that kind of bot!"

	elif 'your mom' in inp or 'ur mom' in inp:
		return "VERY mature :P I'm just trying to have a pleasant conversation with an attractive human (that's you)"

	elif 'fav' in inp and 'prof' in inp:
		return "Blake Howald is hands down the coolest professor ever."

	else:
		return None


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
#	result = analyze("You are stealing my heart.", classifier, dictionary)
#	print result

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
		# tokens = nltk.word_tokenize(response)
		# tagged = nltk.pos_tag(tokens)
		# print tagged
		extra = specialCases(response)
		if extra is not None: print extra
		flirtyWeight = updateFlirtyWeight(analyze(response, classifier, dictionary), flirtyWeight)
		








if __name__ == "__main__":
	main()


##Initiate convo
#tokenize("My Name is Ammar.")