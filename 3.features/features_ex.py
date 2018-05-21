#-*- coding: utf-8 -*-

def char_features(sent):
	
	return list(sent)

def word_features(sent):
	from nltk import word_tokenize
	return word_tokenize(sent)

def stemmed_features(sent):
	from nltk.stem.porter import PorterStemmer

	stemmer = PorterStemmer()

	return [stemmer.stem(w) for w in word_features(sent)]


def pos_features(sent):
	from nltk import pos_tag
	
	return [pos for pos, tag in pos_tag(word_features(sent))]

def tag_features(sent):
	from nltk import pos_tag
	
	return [tag for pos, tag in pos_tag(word_features(sent))]
	
if __name__ == "__main__":
	from nltk import sent_tokenize
	sents = "Along the way, we'll cover some fundamental techniques in NLP, including sequence labeling, n-gram models, backoff, and evaluation. These techniques are useful in many areas, and tagging gives us a simple context in which to present them. We will also see how tagging is the second step in the typical NLP pipeline, following tokenization."
	sentences = sent_tokenize(sents)
	
	for sent in sentences:
		print '##########################'
		print sent 
		print '----char_features------'
		print char_features(sent)
		print '-----word_features-----'
		print word_features(sent)
		print '-----stemmed_features-----'
		print stemmed_features(sent)
		print '-----pos_features-----'
		print pos_features(sent)
		print '-----tag_features-----'
		print tag_features(sent)
		print 
