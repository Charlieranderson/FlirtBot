import nltk
from nltk.tokenize import word_tokenize
  
training_list = []
flirty_file = "FlirtyTexts.txt"
not_flirty_file = "Boring_Corpus"
flirty = open(flirty_file,"r")
not_flirty = open(not_flirty_file, "r")
for line in flirty.readlines():
    if line != "\n":
        training_list.append(tuple((line.strip(), "flirty")))
for line in not_flirty.readlines():
    if line != "\n":
        training_list.append(tuple((line.strip(), "not flirty")))
    
dictionary = set(word.lower() for passage in training_list for word in word_tokenize(passage[0]))

print(dictionary)
  
t = [({word: (word in word_tokenize(x[0])) for word in dictionary}, x[1]) for x in training_list]

print(t)

classifier = nltk.NaiveBayesClassifier.train(t)
  
test_data = "Manchurian was hot and spicy"
test_data_features = {word.lower(): (word in word_tokenize(test_data.lower())) for word in dictionary}
  
print (classifier.classify(test_data_features))