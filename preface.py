# Find all words ending in ing in my paper
for line in open("data/file.txt"):
    for word in line.split():
	if word.endswith('ing'):
	    print word
# download the nltk_data
# -----
# import nltk
# nltk.download()

