# -*- encoding:utf-8 -*- 
#
# 영화평 데이터에 대한 긍정/부정 평가 분류 
#

from codecs import open as copen 
from nltk import word_tokenize
import numpy as np
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import GaussianNB

tr_fname = 'train_ratings.txt' # 학습 파일
test_fname = 'test_ratings.txt'# 테스트 파일

# 데이터 읽어오기 
with copen(tr_fname, 'r', 'utf-8') as trf:
  tr_lines = trf.read().split('\n')
tr_lines = [line.split('\t')[1:] for line in tr_lines]
tr_lines = [(word_tokenize(r), int(l))  for r, l in tr_lines]
tr_size = len(tr_lines)
print('train_size: ', tr_size)
print('train[0]: ', ' '.join(tr_lines[0][0]), tr_lines[0][1])

with copen(test_fname, 'r', 'utf-8') as testf:
  test_lines = testf.read().split('\n')
test_lines = [line.split('\t')[1:] for line in test_lines]
test_lines = [(word_tokenize(r), int(l)) for r, l in test_lines]
test_size = len(test_lines)
print('test_size: ', test_size)
print('test[0]: ', ' '.join(test_lines[0][0]), test_lines[0][1])
print()
# build vocabulary

vocab = {}
for rating, label in tr_lines:
  for w in rating:
    if w not in vocab:
      vocab[w] = len(vocab)
vocab_size = len(vocab)
print('vocabulary size: ', vocab_size)

# 학습 데이터 구축
tr_X = np.zeros(shape=(tr_size, vocab_size))
tr_y = np.zeros(tr_size)
for tid, (rating, label) in enumerate(tr_lines):
  tr_y[tid] = label
  for w in rating:
    vid = vocab[w]
    tr_X[tid][vid] = 1
print('train shape', tr_X.shape, tr_y.shape)

# 테스트 데이터 구축 
test_X = np.zeros(shape=(test_size, vocab_size))
test_y = np.zeros(test_size)
for tid, (rating, label) in enumerate(test_lines):
  test_y[tid] = label
  for w in rating:
    if w in vocab:
      vid = vocab[w]
      test_X[tid][vid] = 1

print('test shape', test_X.shape, test_y.shape)
print()

# naive bayes 분류기 테스트 
print('-----naive bayes-----')
clf = GaussianNB() 
clf.fit(tr_X, tr_y)
print('GaussianNB predict ',' '.join(test_lines[0][0])) 
print('prediction:',  clf.predict([test_X[0]]))
print('actual label:', test_lines[0][1])
print('total test score: ',clf.score(test_X, test_y))

# Linear SVM 분류기 테스트 
print('-----linear svm-----')
clf = LinearSVC()
clf.fit(tr_X, tr_y)
print('LinearSVM predict ',' '.join(test_lines[0][0]))
print('prediction:',  clf.predict([test_X[0]]))
print('actual label:', test_lines[0][1])
print('total test score: ', clf.score(test_X, test_y) )

