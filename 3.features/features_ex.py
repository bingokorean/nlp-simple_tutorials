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
    sent = "Along the way, we'll cover some fundamental techniques in NLP, including sequence labeling, n-gram models, backoff, and evaluation. "

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
