from django.shortcuts import render, redirect
from sklearn.naive_bayes import BernoulliNB
from sklearn.neural_network import MLPClassifier
import xlrd
import numpy as np
import pandas as pd
import sys
import time
from .urlaction import URLCheck
from .Prediction import predict_nn


def getprediction(url):
    try:
        u = URLCheck()
        res = u.validation(url)

        # ---------------------
        if URLCheck.ipaddress(url):
            f1 = 1
        else:
            f1 = 0
        # ---------------------
        if URLCheck.favicon(url):
            f8 = 1
        else:
            f8 = 0
        # ---------------------
        if URLCheck.extractPort(url):
            f9 = 0
        else:
            f9 = 1
        # ---------------------
        print("length of url==", len(url))
        if len(url) > 24:
            f2 = 0
        else:
            f2 = 1
        # ---------------------
        if url.find('@') == -1:
            f4 = 0
        else:
            f4 = 1
        # -----------------------
        if url.count('//') > 7:
            f5 = 0
        else:
            f5 = 1
        # ------------------
        # --------------------
        if url.find('-') == -1:
            f6 = 1
        else:
            f6 = 0
        # --------------------
        if url.count('.') > 2:
            f7 = 0
        else:
            f7 = 1
        # --------------------
        if url.find('https') == -1:
            f10 = 0
        else:
            f10 = 1
        # --------------------
        if url.find('mailto') == -1:
            f15 = 0
        else:
            f15 = 1
        ####################################
        row1 = ["f1", "f2", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f15"]
        row = [f1, f2, f4, f5, f6, f7, f8, f9, f10, f15]
        print(row, "<<<<<<<<Row")
        import csv
        with open('test.csv', 'w') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row1)
            writer.writerow(row)
            csvFile.close()
        res = predict_nn()
        print(res)

        return float(res)
    except Exception as e:
        return 0.0
