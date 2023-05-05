import sys
import pandas as pd
import numpy as np
from sklearn.naive_bayes import BernoulliNB
from sklearn.neural_network import MLPClassifier
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix
import pickle

class Features:

    def train(algo):
        alg=None

        if algo=='nb':
            alg=BernoulliNB()
        

        if algo=='nn':
            alg=MLPClassifier()
        

        if algo=='svm':
            alg=svm.LinearSVC()
        
        

        if algo=='dt':
            alg=DecisionTreeClassifier()
        


        train_file="FeaturesDataset.csv"
        df = pd.read_csv(train_file)
        
        y = np.array(df['Result'])
        X = np.array(df.drop(['Result'], 1))

        alg=alg.fit(X, y)

        test_file='FeaturesTesting.csv'
        tf = pd.read_csv(test_file)
        comp=tf["Result"]
        tf = tf.drop(['Result'], 1)
        testdata = np.array(tf)
        testdata = testdata.reshape(len(testdata), -1)
        predicted_class = alg.predict(testdata)
        accuracy=Features.model_assessment(comp, predicted_class)
        print(accuracy)
        return accuracy


        
    def model_assessment(y_test, predicted_class):
        print('accuracy')
        # Accuracy = (TP + TN) / ALL
        accuracy = accuracy_score(y_test, predicted_class)
        return accuracy



if __name__ == "__main__":
    Features.train('nb')

