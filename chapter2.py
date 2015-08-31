# Chapter 2

## Import NLTK - includes texts fromProject gutenberg http://www.gutenberg.org

import nltk
# See file identifiers in this corpus
# nltk.corpus.gutenberg.fields()  -- p.40  book using an old version of NLTK must use:
fieldids = nltk.corpus.gutenberg.fileids()
print(fieldids)


# pick out one text from gutenberg texts

emma = nltk.corpus.gutenberg.words('austen-emma.txt')
len(emma)
#out: 192427

# performing concordancing and other tasts similar to chapter 1
emma = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
emma.concordance(surprise)

from nltk.corpus import gutenberg
gutenberg.fileids() # does not work in current version on NLTK?

#write a program to display other information about each text,
#buy looping over all the valus of fieldid corresponding to the
#gutenberg file

for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
    print int(num_chars/num_words), int(num_words/num_sents), int(num_words/num_vocab), fileid

#out:
#4 24 26 austen-emma.txt
#4 26 16 austen-persuasion.txt
#4 28 22 austen-sense.txt
#4 33 79 bible-kjv.txt
#4 19 5 blake-poems.txt
#4 19 14 bryant-stories.txt
#4 17 12 burgess-busterbrown.txt
#4 20 12 carroll-alice.txt
#4 20 11 chesterton-ball.txt
#4 22 11 chesterton-brown.txt
#4 18 10 chesterton-thursday.txt
#4 20 24 edgeworth-parents.txt
#4 25 15 melville-moby_dick.txt
#4 52 10 milton-paradise.txt
#4 11 8 shakespeare-caesar.txt
#4 12 7 shakespeare-hamlet.txt
#4 12 6 shakespeare-macbeth.txt
#4 36 12 whitman-leaves.txt

# raw does no text processing for example how many characters are in:
len(gutenberg.raw('blake-poems.txt'))
#38153

#sent function divides the text up into sentences
macbeth_sentences = gutenberg.sents('shakespeare-macbeth.txt')
macbeth_sentences
macbeth_sentences[1037]
#[u'Good', u'night', u',', u'and', u'better', u'health', u'Attend', u'his', u'Maiesty']
longest_len = max([len(s) for s in macbeth_sentences])
[s for s in macbeth_sentences if len(s) == longest_len]

# WEB AND CHAT Text p. 42

from nltk.corpus import webtext
for fileid in webtext.fileids():
    print fileid, webtext.raw(fileid)[:65], '...'

from nltk.corpus import nps_chat
chatroom = nps_chat.posts('10-19-20s_706posts.xml')
chatroom[123]

#brown corpus
#good for stylistics
from nltk.corpus import brown
brown.categories()
brown.words(categories='news'
brown.words(fileids=['cg22'])
brown.sents(categories=['news', 'editofiral','reviews'])

from nltk.corpus import brown
news_text = brown.words(categories='news')
fdist = nltk.FreqDist([w.lower() for w in news_text])
modals = ['can', 'could', 'may', 'might', 'must', 'will']
for m in modals:
    print m + ':', fdist[m],
# out: can: 94 could: 87 may: 93 might: 38 must: 53 will: 389

# NLTK Conditional Frequencies
# cannot get this code to work!!
cfd = nltk.ConditionalFreqDist(
        (genre, word)
       for genre in brown.categories()
       for word in brown.words(categories=genre))

genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
modals = ['can', 'could', 'may', 'might', 'must', 'will']
cfd.tabulate(conditions=genres, samples=modals)
#                 can could  may might must will
#           news   93   86   66   38   50  389
#       religion   82   59   78   12   54   71
#        hobbies  268   58  131   22   83  264
#science_fiction   16   49    4   12    8   16
#        romance   74  193   11   51   45   43
#          humor   16   30    8    8    9   13

#Reuters corpus
## documents are classified into 90 topics and two sets: training and test
## splitting for training and testing is covered in Chapter 6
from nltk.corpus import reuters
reuters.fileids()
## fileids are formatted e.g. test/14826, training/988
reuters.categories()
# out: u'acq', u'alum', u'barley', u'bop', u'carcass', u'castor-oil', u'cocoa', u'coconut', u'coconut-oil', u'coffee', u'copper',

#  !! important to note this corpus the categories overlap

reuters.categories('training/9865')
# out: [u'barley', u'corn', u'grain', u'wheat']
reuters.categories(['training/9865', 'training/9880'])
# out: [u'barley', u'corn', u'grain', u'money-fx', u'wheat'][u'barley', u'corn', u'grain', u'money-fx', u'wheat']
reuters.fileids('barley')
# out: [u'test/15618', u'test/15649', u'test/15676', u'test/15728', ...
reuters.fileids(['barley', 'corn'])
# out: [u'test/14832', u'test/14858', u'test/15033', u'test/15043', u'test/15106', u'test/15287',...

#pulling out a set of words, the first words in upcase are the title
reuters.words('training/9865')[:14]
# [u'FRENCH', u'FREE', u'MARKET', u'CEREAL', u'EXPORT', u'BIDS',
# u'DETAILED', u'French', u'operators', u'have', u'requested', u'licences',
#u'to', u'export']
reuters.words(['training/9865', 'training/9880'])
# out: [u'FRENCH', u'FREE', u'MARKET', u'CEREAL', u'EXPORT', ...]
reuters.words(categories='barley')
# [u'FRENCH', u'FREE', u'MARKET', u'CEREAL', u'EXPORT', ...]
reuters.words(categories=['barley', 'corn'])
# [u'THAI', u'TRADE', u'DEFICIT', u'WIDENS', u'IN', ...]

# INAUGURAL ADDRESS corpus

from nltk.corpus import inaugural
inaugural.fileids()
# out: [u'1789-Washington.txt', u'1793-Washington.txt', u'1797-Adams.txt', u'1801-Jefferson.txt', u'1805-Jefferson.txt', u'1809-Madison.txt'...
# grab the first 4 chars of the fileids to grab the years
[fileid[:4] for fileid in inaugural.fileids()]
# out: [u'1789', u'1793', u'1797', u'1801', u'1805',...
cfd = nltk.ConditionalFreqDist(
        (target, fileid[:4])
        for fileid in inaugural.fileids()
        for w in inaugural.words(fileid)
        for target in ['america', 'citizen']
        if w.lower().startswith(target)) #convert corpus to lowercase then check whether they start with either the targets america or citizen
# requires matplotlib
cfd.plot()

# ANNOTATED TEXT CORPORA

# Loading your own corpus
# see Pathology project: need to add pathology report text to txt files
# using just a folder on my computer
from nltk.corpus import PlaintextCorpusReader
corpus_root = '/usr/share/dict'
wordlists = PlaintextCorpusReader(corpus_root, '.*')
wordlists.fileids()
# ['README', 'connectives', 'propernames', 'web2', 'web2a', 'words']

wordlists.words('connectives')
# [u'the', u'of', u'and', u'to', u'a', u'in', u'that', ...]

#Counting words by genre
from nltk.corpus import brown
cfd = nltk.ConditionalFreqDist(
        (genre, word)
        for genre in brown.categories()
        for word in brown.words(categories=genre))

genre_word = [(genre, word) # producing pairs consisting of the genre and the word
        for genre in ['news', 'romance'] # for each genre...
        for word in brown.words(categories=genre)] # loop over every word in the genre
len(genre_word
#out: 170576

genre_world[:4]
#[('news', u'The'), ('news', u'Fulton'), ('news', u'County'), ('news', u'Grand')]
# pairs at the beginning of the list genre_word will be of the form ('news', word)

genre_word[-4:]
# at the end of genre_word will be the form of ('romance', word)

cfd = nltk.ConditionalFreqDist(genre_word)
    cfd # we can type the name of the variable to inspect it

cfd.conditions()
# out:['romance', 'news'] and varify it has two conditions
