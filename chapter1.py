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




