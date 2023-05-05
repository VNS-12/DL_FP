import sys
import pandas as pd
from sklearn.pipeline import Pipeline
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, f1_score, accuracy_score, precision_score, recall_score, confusion_matrix
import pickle
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score


# This class loads the testing.csv dataset and calculate the accuracy of the algorithms

class Testing:

    def detecting(model,test_file):

        data1 = pd.read_csv(test_file)
        print(len(data1))
        y = data1['label']
        test=data1['content']
        

        filename = model
        train = pickle.load(open(filename, 'rb'))
        print()
        predicted_class = train.predict(test)
        print(predicted_class)
        acc=Testing.model_assessment(y, predicted_class)
        return acc
        

    def model_assessment(y_test, predicted_class):
        print('accuracy')
        # Accuracy = (TP + TN) / ALL
        accuracy = accuracy_score(y_test, predicted_class)

        #Recall = TP / (TP + FN)
        return (accuracy)



if __name__ == "__main__":
    print(Testing.detecting('nn_model.sav','TextTesting.csv'))
    print(Testing.detecting('nb_model.sav','TextTesting.csv'))

    print(Testing.detecting('svm_model.sav','TextTesting.csv'))


