import numpy as np
import pandas as pd

test = []
train = []

data_set = 'ml-latest-small'
data_raw = pd.read_csv('data/'+data_set+'/ratings.csv')

usr_num = data_raw.tail(1).iloc[0,0]

for i in range(1,usr_num+1):
    
    piece = data_raw[data_raw['userId'] == i]
    train.append(piece[:int(piece.shape[0] * 0.75)])
    test.append(piece[int(piece.shape[0] * 0.75):])
data_train = pd.concat(train)
data_test = pd.concat(test)

data_test.to_csv('data/'+data_set+'/ratings_test.csv')
data_train.to_csv('data/'+data_set+'/ratings_train.csv')




