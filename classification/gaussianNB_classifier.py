# -*- encoding:utf-8 -*-

import numpy as np
from sklearn.naive_bayes import GaussianNB
from iris_data import get_data # data: iris_data.csv; iris_data: 읽어오는 파일 

trainX, trainy, testX, testy = get_data() # data 가져오기 
clf = GaussianNB() # 분류기 객체 생성 
clf.fit(trainX, trainy) # 학습 시킴 
print clf.predict(testX) # test data로 예측한 값 
print testy # 정답 결과 
print clf.score(testX, testy) # 예측 점수 
