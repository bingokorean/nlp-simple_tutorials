#-*- encoding: utf-8 -*-

from konlpy.tag import Kkma
from nltk import sent_tokenize

sentence = u'안녕 나는 지능정보연구실에서 공부하고 있어. 너는 누구니?'
sents = sent_tokenize(sentence) # 문장 자르기 

kkma = Kkma()
print u'######\t모든 형태소\t#####'
for sent in sents:
    analyzed = kkma.pos(sent)
    print ' '.join([pos for pos, tag in analyzed])
    print ' '.join([pos+'/'+tag for pos, tag in analyzed])
    
print u'######\t명사만\t#####'
for sent in sents:
    print ' '.join(kkma.nouns(sent))
