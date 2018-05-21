#-*- coding:utf-8 -*-

sent1 = 'I am a student .'
sent2 = 'I had dinner .'

print 'Words in sentence 1:', sent1.split()
words1 = sent1.split()
words2 = sent2.split()
words = words1 + words2
vocab = list(set(words))
vocab_size = len(vocab)

import numpy as np  # 행렬 라이브러리 numpy

vec1 = np.zeros(vocab_size)  # numpy.zeros(n)은 길이가 n인 0으로 채워진 벡터를 만든다. numpy.ones(n)은 1로 채워진 벡터.
vec2 = np.zeros(vocab_size)


for i in range(vocab_size):
    if words1.count(vocab[i])>0:
        vec1[i] =1 
    if words2.count(vocab[i])>0:
        vec2[i] = 1

print 'vocabulary: ',vocab
print 'first vector:',vec1
print 'second vector:',vec2 
    
