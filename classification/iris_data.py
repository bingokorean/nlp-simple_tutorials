# -*- encoding:utf-8 -*-

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

