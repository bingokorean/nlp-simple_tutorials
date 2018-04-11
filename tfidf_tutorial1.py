#-*- encoding: utf-8 -*-
# created by Meeyeong, modified at 3/27

from sklearn.feature_extraction.text import TfidfVectorizer

data = [u'안녕 나는 오늘 밥을 먹었어',
          u"나는 나는 오늘 학교에 안가기로 했어"]

vectorizer = TfidfVectorizer(min_df=1)
X = vectorizer.fit_transform(data)
idfs = vectorizer.idf_
vocabs = vectorizer.get_feature_names()
print '#######\tidf values\t######'
for vocab, idf in zip(vocabs, idfs):
    print vocab, idf

doc = 0 # first file 
vocab_index = X[doc,:].nonzero()[1] # get vocabulary indexes in the first file
tfidf_scores = zip(vocab_index, [X[doc, x] for x in vocab_index])
print '#######\tfirst file tfidf values\t######'
for w, s in [(vocabs[i], s) for (i, s) in tfidf_scores]:
    print w, s

doc = 1 # second file 
vocab_index = X[doc,:].nonzero()[1] # get vocabulary indexes in the second file
tfidf_scores = zip(vocab_index, [X[doc, x] for x in vocab_index])
print '#######\tsecond file tfidf values\t######'
for w, s in [(vocabs[i], s) for (i, s) in tfidf_scores]:
    print w, s

