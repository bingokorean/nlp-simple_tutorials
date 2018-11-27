# -*- encoding:utf-8 -*-
# 데이터 처리 라이브러리 pandas를 사용하여 iris 데이터 읽기 
# pandas: csv 파일 등 데이터 파일을 빠르게 처리 할 수 있는 라이브러리 
# pandas 라이브러리 간단 예제: https://wikidocs.net/22698
# 설치방법: cmd에서 python 설치 라이브러리로 이동하여 Scripts 폴더에서 <pip install pandas> 명령어 입력
# API: https://pandas.pydata.org/pandas-docs/stable/tutorials.html (동영상 링크 있음)
# sklearn: LabelEncoder 함수: 학습과 테스트에 사용할 y값을 숫자 index 로 맵핑해 주는 라이브러리 
# 아래 코드 return 전에 train_y, test_y 를 프린트 해보면 확실히 알수 있다. 
def get_data():
    import pandas as pd
    from sklearn.preprocessing import LabelEncoder

    f = 'iris-data.csv'

    data = pd.read_csv(f)

    setosa = data.loc[data['species']== 'setosa']
    versicolor = data.loc[data['species']== 'versicolor']
    virginica = data.loc[data['species']== 'virginica']

    train_size = 45

    train_data = setosa.loc[:train_size-1].append(versicolor.loc[len(setosa):len(setosa)+train_size-1])
    train_data = train_data.append(virginica.loc[len(setosa)+len(versicolor):len(setosa)+len(versicolor)+train_size-1])
    test_data = setosa.loc[train_size:].append(versicolor.loc[len(setosa)+train_size:])
    test_data = test_data.append(virginica.loc[len(setosa)+len(versicolor)+train_size:])

    train_X = train_data.iloc[:,0:4].as_matrix()
    test_X = test_data.iloc[:,0:4].as_matrix()

    train_y = train_data.iloc[:,4:].T.as_matrix()[0]
    test_y = test_data.iloc[:,4:].T.as_matrix()[0]
    
    le = LabelEncoder()
    le.fit(train_y)
    train_y = le.transform(train_y)
    test_y = le.transform(test_y)
    
    return train_X, train_y, test_X, test_y

