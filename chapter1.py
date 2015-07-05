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

