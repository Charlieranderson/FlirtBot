#To be run every time the corpuses are changed. Generates a list of words from the corpuses and a classifier, which contains a list of tuples (the 1st item of tuple is the dictionary of all words and whether they are in the sentence and the 2nd item of tuple is whether the sentence is flirty)

import nltk
from nltk.tokenize import word_tokenize
  
training_list = []
flirty_file = "FlirtyTexts.txt"
not_flirty_file = "Boring_Corpus"
training_data_file = "training_data.txt"
dictionary_file = "dictionary.txt"

flirty = open(flirty_file,"r")
not_flirty = open(not_flirty_file, "r")
dictionary_string = open(dictionary_file, "w")
training_data = open(training_data_file, "w")
for line in flirty.readlines():
    if line != "\n":
        training_list.append(tuple((line.strip(), "flirty")))
for line in not_flirty.readlines():
    if line != "\n":
        training_list.append(tuple((line.strip(), "not flirty")))
    
dictionary = set(word.lower() for passage in training_list for word in word_tokenize(passage[0]))
dictionary_string.write(str(dictionary))
print("yo")

t = [({word: (word in word_tokenize(x[0])) for word in dictionary}, x[1]) for x in training_list]

training_data.write(str(t))