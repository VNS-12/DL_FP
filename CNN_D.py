import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import metrics
import keras
import os.path
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def CnnModel():
    
    dataset = pd.read_csv('FeaturesDataset.csv')
    X = dataset.iloc[:, 0:17].values
    y = dataset['Result']
    print(y)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)

 
    model = Sequential()
    model.add(Dense(activation="relu", input_dim=17, units=7, kernel_initializer="uniform"))
    model.add(Dense(activation="sigmoid", input_dim=17, units=1, kernel_initializer="uniform"))
    model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
    model.fit(X_train, y_train, batch_size=100, nb_epoch=100)
    if os.path.exists("cnn_model.model"):
        pass
    else:
        model.save("cnn_model.model")
    
    cnn = model.predict(X_test)
    acc = (metrics.accuracy_score(y_test, cnn.round())*100)
    print("Accuracy Score CNN :",acc)
    pr_score = (metrics.precision_score(y_test,cnn.round())*100)
    print("Precision Score :",pr_score)
    R_score = (metrics.precision_score(y_test, cnn.round())*100)
    print("Recall Score :", R_score)
    F1_score = (metrics.precision_score(y_test, cnn.round())*100)
    print("F1 Score :", F1_score)

    return acc


if __name__ == '__main__':
    CnnModel()




