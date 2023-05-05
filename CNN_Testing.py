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
from keras.models import Sequential, load_model



def CnnModel():
    model_path = 'cnn_model.model'
    model = load_model(model_path)
    print("CNN Model Loaded")

    dataset = pd.read_csv('FeaturesTesting.csv')
    y = np.array(dataset['Result'])
    X = np.array(dataset.drop(['Result'], 1))
    
    cnn = model.predict(X)
    for x in cnn:
        print(x[0].round())

    acc = (metrics.accuracy_score(y, cnn.round()))
    print("Accuracy Score CNN :",acc)
   
    return (acc)

if __name__ == '__main__':
    CnnModel()




