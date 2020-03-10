# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:26:12 2020

@author: abhisek
"""
import csv

with open("wpi_monthly_data.csv") as f:
    lis = [line.split() for line in f]
    lis1=[]        # create a list of lists
    dates=(lis[0][0].split(","))
    dates=dates[3:]
    for i in dates:
        date=i.split('"')[1]
        lis1.append(date)
    print(dates)
    petro=(lis[138][1].split(","))
    petro=petro[3:]
    print(len(dates))
    print(len(petro))
    lis2=[]
    for i in petro:
        price=i.split('"')[1]
        lis2.append(price)
        
        
    with open("petroleum.tsv","wt") as out_file:
        tsv_writer=csv.writer(out_file,delimiter='\t')
        tsv_writer.writerow(["Date","Value"])
        for i in range(0,len(dates)):
            if(lis2[i]!="NA"):
                tsv_writer.writerow([lis1[i],float(lis2[i])])
            else:
                break
    with open("petroleum_test.tsv","wt") as test_file:
                    tsv_writer=csv.writer(test_file,delimiter='\t')
                    tsv_writer.writerow(["Date","Value"])
                    for i in range(0,len(dates)):
                        if(lis2[i]=="NA"):
                            tsv_writer.writerow([lis1[i],0])
                        else:
                            tsv_writer.writerow([lis1[i],float(lis2[i])])

                
                    

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset=pd.read_csv("petroleum.tsv",delimiter='\t',quoting=3,encoding='latin-1')
train=dataset.iloc[:,1:2].values

from sklearn.preprocessing import MinMaxScaler
sc=MinMaxScaler(feature_range=(0,1))
train_scaled=sc.fit_transform(train)

X_train=[]
y_train=[]

for i in range(30,len(train_scaled)):
    X_train.append(train_scaled[i-30:i,0])
    y_train.append(train_scaled[i,0])
X_train,y_train=np.array(X_train),np.array(y_train)

X_train=np.reshape(X_train,(X_train.shape[0],X_train.shape[1],1))




from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout


regressor=Sequential()


regressor.add(LSTM(units=50,return_sequences=True,input_shape=(X_train.shape[1],1)))
regressor.add(Dropout(0.2))

regressor.add(LSTM(units=50,return_sequences=True))
regressor.add(Dropout(0.2))


regressor.add(LSTM(units=50,return_sequences=True))
regressor.add(Dropout(0.2))

regressor.add(LSTM(units=50))
regressor.add(Dropout(0.2))

regressor.add(Dense(units=1))

regressor.compile(optimizer='adam',loss='mean_squared_error')

regressor.fit(X_train,y_train,epochs=500,batch_size=32)



dataset_test=pd.read_csv('petroleum_test.tsv',delimiter='\t',quoting=3,encoding='latin-1')

inputs=dataset_test.iloc[:,1:2].values
plot_og=inputs[30:]
inputs=inputs.reshape(-1,1)
inputs=sc.transform(inputs)
X_test=[]

for i in range(30,len(inputs)):
    X_test.append(inputs[i-30:i,0])
X_test=np.array(X_test)
X_test=np.reshape(X_test,(X_test.shape[0],X_test.shape[1],1))

predicted=regressor.predict(X_test)
predicted=sc.inverse_transform(predicted)

plt.plot(plot_og,color="red",label="Actual Price")
plt.plot(predicted,color="blue",label="Predicted Price")
plt.title("Prediction")
plt.xlabel("Time")
plt.ylabel("Value of Commodity")
plt.legend()
plt.show()












        
        