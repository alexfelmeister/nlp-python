# 1.1
from nltk.book import *

# search text for word
text1.concordance("monstrous")
text3.concordance("lived")
text5.concordance("lol")

text1.similar("monstrous")

text2.common_contexts(["monstrous", "very"])

# requires numpy abd matplotlib
text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])

# generate random text (? more in chapter 3)
text3.generate()

# counting vocabulary
# Length of text from start to finish
len(text3)
# obtain vocabulary items of text3
set(text3)

# set of words in order along with symbols
sorted(set(text3))

# calculate the measure of the lexical richness of the text
from __future__ import division
len(text3) / len(set(text3))

# count how often a word occurs in a text

text3.count("smote")
# what percentage of text is taken up by a word
100* text4.count('a') / len (text4)
# how many times lol occurs in chat text  (p.8)
text5.count('lol')

# create functions to repeat above calculations on multiple sets of text

def lexical_diversity(text):
	return len(text) / len(set(text))
	
def percentage(count, total):
	return 100 * count / total
	
	
#	Examples using functions

lexical_diversity(text3)
#16.050197203298673
lexical_diversity(text5)
#7.420046158918563
percentage(4, 5)
#80.0
percentage(text4.count('a'), len(text4))
#1.4643016433938312



# 1.2

# representation of a sequence from moby dick in python

sent1 = ['Call', 'me', 'Ishmael', '.']

# inspect list
sent1

len(sent1)

lexical_diversity(sent1)
# 1

# sent1 - 9 are defined in the nltk.books import

#make up a few sentences and put them into lists

ex1 = ['Monty', 'Python', 'and', 'the', 'Holy', 'Grail']
# trying out some functions from previous section
sorted(ex1)
len(set(ex1))
ex1.count('the')

# concatenation of lists examples

['Monty', 'Python'] + ['and', 'the', 'Holy', 'Grail']

sent4 + sent1

#appending 

sent1.append("Some")
sent1
# ['Call', 'me', 'Ishmael', '.', 'Some']

# Indexing lists using python's index of the data
# conversely can use the length and functions to pull out a word at a point

text4[173]
#'awaken'

# find the index number for the word in the text

text4.index('awaken')
# 173

# this is utilized to slice data to access certain words or sublists of words -- slicing

text5[16715:16735]

text6[1600:1625]

# create an artificial sentence to see subtitles of indexing 

sent = ['word1', 'word2', 'word3', 'word4', 'word5', 'word6', 'word7', 'word8', 'word9', 'word10']

sent[0]

sent[9]
# Example Runtime Error (not syntax)
##>>> sent[10]
##Traceback (most recent call last):
##  File "<stdin>", line 1, in <module>
##IndexError: list index out of range


# Confirmation of indexing 
sent[5:8]
#['word6', 'word7', 'word8']
sent[5]
#'word6'
sent[6]
#'word7'
sent[7]
#'word8'

# Convention of m:n means elements m...n-1
# can omit the first number if the slice begins at the start of the list and we can omit the second number if the slice goes to the end

sent[:3]


# modify element lists
sent[0] = 'First'
sent[9] = 'Last'
len(sent)
#10
sent[1:9] = ['Second', 'Third']
sent
#['First', 'Second', 'Third', 'Last']
sent[9]
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#IndexError: list index out of range


# try out creating a sentence and modify elements and slices
#note created a py file: custom_functions.py to load requirements as I create them
# use- from custom_functions import *

senttry = ['If', 'you', 'can\'t', 'love', 'yourself', 'then', 'how','the','hell','you','gonna','love','somebody','else','?']

# thought: one could scan the lexical diversity for a number and do an action based on that number

# Variables

sent1 = ['Call','me','Ishmael','.']

# examples of variables and assignments

my_sent = ['Bravely','bold','Sir','Robin',',','rode','forth','from','Camelot','.']
noun_phrase = my_sent[1:4]
noun_phrase
# see contents of variable, noun_phrase
wOrDs = sorted(noun_phrase)
wOrDs
# see contents of variable

# using variables to hold intermediate steps of computation to make code easier to follow

vocab = set(text1)
vocab_size = len(vocab)
vocab_size
# results of above computation


# Strings

name = 'Monty' # string to a variable
name[0] # index a string
#'M'
name[:4] # slice a string
#'Mont'

# perform multiplication and additional strings

name * 2
# 'MontyMonty'
name + '!'
#'Monty!'

# join the words of a list to make a single string or split a string into a list
' '.join(['Monty','Python'])
#'Monty Python'
'Monty Python'.split()
#['Monty', 'Python']

# 1.3 COMPUTING WITH LANGUAGE - Simple Statistics

saying = ['After','all','is','said','and','done','more','is','said','than','done']
tokens = set(saying)
tokens = sorted(tokens)
tokens[-2:]

# Frequency Distributions
## Could be important to find vocabulary in text from clinical notes or reports

# inspect number of words (outcomes) that have been counted up
fdist1 = FreqDist(text1)
# 260819 in the case of MobyDick
fdist1
# the expression keys() gives us a list of all distinct types of text
vocabulary1 = fdist1.keys()
# we can look at the first 50 of these by slicing the list
vocabulary1[:50]
# Note this tells us not much about the text. Whale is mentioned a lot, but it just shows a lot of "english plumbing"

# TRY: predicting frequency distribution example for text2. 

fdist2 = FreqDist(text2)
fdist2 
vocabulary2 = fdist2.keys()
vocabulary2[:50]


# Produce a cumulative frequency chart for the words. These 50 words account for nearly half the book!
fdist1.plot(50, cumulative=True)

# words that occur only once are called "hapaxes" , though without content it is hard to tell what they mean.
fdist1.hapaxes()

#most frequent and one-time words are not helpful
# now look for long words, words with more than 15 characters
## see formula on p.19 and implementation in python:
V = set(text1)
long_words = [w for w in V if len(w) > 15]
sorted(long_words)
# ['CIRCUMNAVIGATION', 'Physiognomically', 'apprehensiveness', 'cannibalistically', 'characteristically', 'circumnavigating', 'circumnavigation', 'circumnavigations', 'comprehensiveness', 'hermaphroditical', 'indiscriminately', 'indispensableness', 'irresistibleness', 'physiognomically', 'preternaturalness', 'responsibilities', 'simultaneousness', 'subterraneousness', 'supernaturalness', 'superstitiousness', 'uncomfortableness', 'uncompromisedness', 'undiscriminating', 'uninterpenetratingly']
# try for text 4 to see long words that reflect national focus in state of the union
V = set(text4)
long_words = [w for w in V if len(w) > 15]
sorted(long_words)

# try for text5 to see informal content
V = set(text5)
long_words = [w for w in V if len(w) > 15]
sorted(long_words)

# This still doesnt typify the text. We really want to find long words that are repeated
## this could eliminate frequent short words (e.g. the) and infrequent long words (e.g. antiphilosophists)

fdist5 = FreqDist(text5)
sorted([w for w in set(text5) if len(w) > 7 and fdist[w] > 7])
#['#14-19teens', '#talkcity_adults', '((((((((((', '........', 'Question', 'actually', 'anything', 'computer', 'cute.-ass', 'everyone', 'football', 'innocent', 'listening', 'remember', 'seriously', 'something', 'together', 'tomorrow', 'watching']

# two conditions: 
## len(w) > 7 ensures that words are longer than 7 letters
## fdist5[w] > 7 ensures words occur more than 7 times

# Collocations and Bigrams
## Collocation - sequence of words that occur together often (e.g. red wine)
## COLOCATIONS ARE FREQUENT BIGRAMS
## user the bigrams function to find pairs of words
bigrams(['more','is','said','than','done'])
#[('more', 'is'), ('is', 'said'), ('said', 'than'), ('than', 'done')]

# We want to fucus on cases that involve rare words. 
# Need bigrams that occure more often than we would expect based on the frequency of individual words
# collocations() function does this

text4.collocations()

text8.collocations()

[len(w) for w in text1]

fdist = FreqDist([len(w) for w in text1])
fdist
# <FreqDist with 19 samples and 260819 outcomes>
# ^ is a distribution containing a quarter of a million items, each of which is a number corresponding to a word taken out of the test
# there are only 20 distinct items being counted, the numbers 1 - 20

fdist.items()
# [(3, 50223), (1, 47933), (4, 42345), (2, 38513), (5, 26597), (6, 17111), (7, 14399), (8, 9966), (9, 6428), (10, 3528), (11, 1873), (12, 1053), (13, 567), (14, 177), (15, 70), (16, 22), (17, 12), (18, 1), (20, 1)]
fdist.max()
# 3
fdist[3]
# 50223
fdist.freq(3)
# 0.19255882431878046
# above we see the most frequent word length is 3 and that words of length 3 account for roughly 50,000 of the words in the book. 

# 1.4 Making decisions and taking control (operators)

sent7 # First sentecne from text7 well street journal
# ['Pierre', 'Vinken', ',', '61', 'years', 'old', ',', 'will', 'join', 'the', 'board', 'as', 'a', 'nonexecutive', 'director', 'Nov.', '29', '.']
[w for w in sent7 if len(w) < 4]
# [',', '61', 'old', ',', 'the', 'as', 'a', '29', '.']
[w for w in sent7 if len(w) <= 4]
#[',', '61', 'old', ',', 'will', 'join', 'the', 'as', 'a', 'Nov.', '29', '.']
[w for w in sent7 if len(w) == 4]
#['will', 'join', 'Nov.']
[w for w in sent7 if len(w) !=  4]
#['Pierre', 'Vinken', ',', '61', 'years', 'old', ',', 'the', 'board', 'as', 'a', 'nonexecutive', 'director', '29', '.']

# [w for w.... ] is a python test where condition that yields either true or false. 

sorted([w for w in set(text1) if w.endswith('ableness')]) # words in texst1 that end with 'ableness'
#['comfortableness', 'honourableness', 'immutableness', 'indispensableness', 'indomitableness', 'intolerableness', 'palpableness', 'reasonableness', 'uncomfortableness']

sorted([term for term in set(text4) if 'gnt' in term])
# ['Sovereignty', 'sovereignties', 'sovereignty']

sorted([item for item in set(text6) if item.istitle()])
# ['A', 'Aaaaaaaaah', 'Aaaaaaaah', 'Aaaaaah', 'Aaaah', 'Aaaaugh', 'Aaagh', 'Aaah', 'Aaauggh', 'Aaaugh', 'Aaauugh', 'Aagh', 'Aah', 'Aauuggghhh', 'Aauuugh',....

sorted([item for item in set(sent7) if item.isdigit()])
# ['29', '61']

sorted([w for w in set(text7) if '-' in w and 'index' in w])
# ['Stock-index', 'index-arbitrage', 'index-fund', 'index-options', 'index-related', 'stock-index']

sorted([wd for wd in set(text3) if wd.istitle() and len(wd) > 10])
#['Abelmizraim', 'Allonbachuth', 'Beerlahairoi', 'Canaanitish', 'Chedorlaomer', 'Girgashites', 'Hazarmaveth', 'Hazezontamar', 'Ishmeelites', 'Jegarsahadutha', 'Jehovahjireh', 'Kirjatharba', 'Melchizedek', 'Mesopotamia', 'Peradventure', 'Philistines', 'Zaphnathpaaneah']

sorted([w for w in set(sent7) if not w.islower()])
# [',', '.', '29', '61', 'Nov.', 'Pierre', 'Vinken']

sorted([t for t in set(text2) if 'cie' in t or 'cei' in t])
# ['ancient', 'ceiling', 'conceit', 'conceited', 'conceive', 'conscience', 'conscientious', 'conscientiously', 'deceitful', 'deceive', 'deceived', 'deceiving', 'deficiencies', 'deficiency', 'deficient', 'delicacies', 'excellencies', 'fancied', 'insufficiency', 'insufficient', 'legacies', 'perceive', 'perceived', 'perceiving', 'prescience', 'prophecies', 'receipt', 'receive', 'received', 'receiving', 'society', 'species', 'sufficient', 'sufficiently', 'undeceive', 'undeceiving']

# Operating on every element

[len(w) for w in text1]
# i think gives each word and it's length
[w.upper() for w in text1]
# the function operates on a word to compute its length or to convert it to uppercase.

len(text1)
# 260819
len(set(text1))
# 19317
len(set([word.lower() for word in text1]))
# 17231
# ^ now that we are not double-counting words like This and this, which differ only in capitalization, we've wiped 2,000 off the vocabulary count. 
# We can go a step further and eliminate numbers and punctuation from the vocabulary count buy filtering out any non-alphabetic items: 

# lowercases all the purely alphabetic items. 
len(set([word.lower() for word in text1 if word.isalpha()]))
# 16948

# Nested code blocks

# WE can use nested code blocks to create a variable called word containing the string value 'cat'
# If statement checks whether the test len(word) < 5. It is, so the boy of the if statement is ivoked and the print statement is executed.

word = 'cat'
if len(word) < 5:
	print 'word length is less than 5'


# Change the conditional test to len(word) >= 5 to check that the length of word is greater than or equal to 5 then the test will no longer be true
if len(word) >= 5:
	print 'word length is greater than or equal to 5'

# an if statement is known as a control structure because it controls whether the code in the intended block will be run

for word in ['Call', 'me', 'Ismael', '.']:
	print word
	
#Call
#me
#Ismael
#.
## This is a loop because the code is in circular fashion. It starts by performing the assignment wrod = 'Call' 


# Looping with conditions p.26
# In the example loop over every item of the list and print the item only if it ends with the letter l.

sent1 = ['Call', 'me', 'Ishmael', '.']
for xyzzy in sent1:
	if xyzzy.endswith('l'):
		print xyzzy
#Call
#Ishmael


# specify an action to be taken if the condition in the if is met, then  if the else if and the else.
for token in sent1:
     if token.islower():
             print token, 'is a lowercase word'
     elif token.istitle():
             print token, 'is a titlecase word'
     else:
             print token, 'is punctuation'

# Call is a titlecase word
# me is a lowercase word
# Ishmael is a titlecase word
# . is punctuation

# create a list of cie and cei words, then loop over each item and print it
# comma at the end of the print statement produces the output in a single line
tricky = sorted([w for w in set(text2) if 'cie' in w or 'cei' in w])
for word in tricky:
	print word,
## ancient ceiling conceit conceited conceive conscience conscientious conscientiously deceitful deceive deceived deceiving deficiencies deficiency deficient delicacies excellencies fancied insufficiency insufficient legacies perceive perceived perceiving prescience prophecies receipt receive received receiving society species sufficient sufficiently undeceive undeceiving

