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

import xlrd
from .Predict import getprediction
from .WebText import WebText
from .TextPrediction import TextPrediction

fres = 0;
fres2 = 0;
tres = 0;
tot = 0;


def predict():
    fres = 0;
    tres = 0;
    tot = 0;
    fres2=0;

    try:
        book = xlrd.open_workbook('TestFile.xlsx')
        sheet = book.sheet_by_index(0)
        o = open('res.txt', 'w')
        for r in range(0, sheet.nrows):
            f0 = sheet.cell(r, 0).value
            f1 = sheet.cell(r, 1).value
            url = f0
            act = int(f1)

            tot = tot + 1
            res1 = getprediction(url)
            print(res1, '@@@@@@@@@@@')
            res1 = int(res1)
            text = WebText.get(url)
            res2 = TextPrediction.detecting(text)
            if res2=='good':
                res2=1
            else:
                res2=0
            o.write(url + '	r1=' + str(res1) + '	r2' + str(res2) + '		a=' + str(act) + '\n')

            tres=tres+1

            if res1 == act:
                fres = fres + 1

            if res2 == act:
                fres2 = fres2 + 1

        print(fres, fres2)
        return(tres,fres,fres2)
    
    except Exception as e:
        print(e)

if __name__ == '__main__':
    predict()
