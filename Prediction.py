# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\QT\phishing\niave.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!


from sklearn.neural_network import MLPClassifier
import pickle
import numpy as np
import pandas as pd
import sys
import time
from sklearn import metrics



def predict_nn():
    try:
        fn=[1, 0, 0, 1, 0, 0, 1, 1, 1, 0]
        # list=[f1,f2,f3,f4,f5,f6,f8,f9,f10,f15]



        #print("sssss",pd.read_csv("E://test.csv"))
        tf = pd.read_csv("test.csv")
        print(tf,"<----------")

        testdata = np.array(tf)
        print("td=", testdata)
        testdata = testdata.reshape(len(testdata), -1)
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^', testdata)


        s = time.clock()


        filename = 'nn_features.sav'

        train = pickle.load(open(filename, 'rb'))
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^')

        predicted_class = train.predict(testdata)
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^')

        e = time.clock()
        t = round(e - s, 5)
        print("elm:", t, "s")
        print("pre=", predicted_class[0])
        return predicted_class[0]


    except Exception as e:
        print("Error=" + e.args[0])
        tb = sys.exc_info()[2]
        print(tb.tb_lineno)


if __name__ == '__main__':
    predict_nn()