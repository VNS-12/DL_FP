from django.shortcuts import render, redirect
from sklearn.naive_bayes import BernoulliNB
from sklearn.neural_network import MLPClassifier
from django.http import HttpResponse, request
from .models import onlineuser

from .models import graph

from django.core import serializers
from django.template import Context
import xlrd
import numpy as np
import pandas as pd
import sys
import time
from sklearn import metrics
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix
import matplotlib.pyplot as plt;
from .urlaction import URLCheck
from .Prediction import predict_nn
from PIL import Image


def home(request):
    return render(request, 'index.html')


def userhomedef(request):
    if "useremail" in request.session:
        uid = request.session["useremail"]
        d = onlineuser.objects.filter(email__exact=uid)
        return render(request, 'user_home.html', {'data': d[0]})

    else:
        return render(request, 'user.html')


def adminhomedef(request):
    if "adminid" in request.session:
        uid = request.session["adminid"]
        return render(request, 'admin_home.html')

    else:
        return render(request, 'admin.html')


def userlogoutdef(request):
    try:
        del request.session['useremail']
    except:
        pass
    return render(request, 'user.html')


def adminlogoutdef(request):
    try:
        del request.session['adminid']
    except:
        pass
    return render(request, 'admin.html')


def adminlogindef(request):
    return render(request, 'admin.html')


def userlogindef(request):
    return render(request, 'user.html')


def signupdef(request):
    return render(request, 'signup.html')


def usignupactiondef(request):
    email = request.POST['mail']
    pwd = request.POST['pwd']
    zip = request.POST['zip']
    name = request.POST['name']
    age = request.POST['age']
    gen = request.POST['gen']

    d = onlineuser.objects.filter(email__exact=email).count()
    if d > 0:
        return render(request, 'signup.html', {'msg': "Email Already Registered"})
    else:
        d = onlineuser(name=name, email=email, pwd=pwd, zip=zip, gender=gen, age=age)
        d.save()
        return render(request, 'signup.html', {'msg': "Register Success, You can Login.."})

    return render(request, 'signup.html', {'msg': "Register Success, You can Login.."})


def userloginactiondef(request):
    if request.method == 'POST':
        uid = request.POST['mail']
        pwd = request.POST['pwd']
        d = onlineuser.objects.filter(email__exact=uid).filter(pwd__exact=pwd).count()

        if d > 0:
            d = onlineuser.objects.filter(email__exact=uid)
            request.session['useremail'] = uid
            return render(request, 'user_home.html', {'data': d[0]})

        else:
            return render(request, 'user.html', {'msg': "Login Fail"})

    else:
        return render(request, 'user.html')


def adminloginactiondef(request):
    if request.method == 'POST':
        uid = request.POST['uid']
        pwd = request.POST['pwd']

        if uid == 'admin' and pwd == 'admin':
            request.session['adminid'] = 'admin'
            return render(request, 'admin_home.html')

        else:
            return render(request, 'admin.html', {'msg': "Login Fail"})

    else:
        return render(request, 'admin.html')


def features(request):
    if "adminid" in request.session:

        return render(request, 'features.html')

    else:
        return render(request, 'admin.html')


def nntest(request):
    if "adminid" in request.session:
        return render(request, 'nntest.html')

    else:
        return render(request, 'admin.html')
def cnntest(request):
    if "adminid" in request.session:
        return render(request, 'cnntest.html')

    else:
        return render(request, 'admin.html')

def dttest(request):
    if "adminid" in request.session:
        return render(request, 'dttest.html')

    else:
        return render(request, 'admin.html')


def naivetest(request):
    if "adminid" in request.session:
        return render(request, 'naivetest.html')
    else:
        return render(request, 'admin.html')


def svmtest(request):
    if "adminid" in request.session:
        return render(request, 'svmtest.html')
    else:
        return render(request, 'admin.html')


def naiveprediction(request):
    if "adminid" in request.session:

        from .Features import Features
        acc = Features.train('nb')

        # s=graph.objects.update(naive=accuracy)
        s = graph.objects.all().delete()
        d = graph(naive=float(acc), nn=0, svm=0, dt=0, cnn=0)
        d.save()

        return render(request, 'nbresults.html', {'msg': acc})

    else:
        return render(request, 'admin.html')


def svmprediction(request):
    if "adminid" in request.session:

        from .Features import Features
        acc = Features.train('svm')

        # s=graph.objects.update(naive=accuracy)
        s = graph.objects.update(svm=acc)

        return render(request, 'svmresults.html', {'msg': acc})

    else:
        return render(request, 'admin.html')


def nnprediction(request):
    if "adminid" in request.session:

        from .Features import Features
        acc = Features.train('nn')

        s = graph.objects.update(nn=acc)

        return render(request, 'nnresults.html', {'msg': acc})

    else:
        return render(request, 'admin.html')


def cnnprediction(request):
    if "adminid" in request.session:

        from .CNN_D import CnnModel
        CnnModel()
        from .CNN_Testing import CnnModel
        acc = CnnModel()

        s = graph.objects.update(cnn=acc)

        return render(request, 'cnnresults.html', {'msg': acc})

    else:
        return render(request, 'admin.html')

def dtprediction(request):
    if "adminid" in request.session:

        from .Features import Features
        acc = Features.train('dt')

        s = graph.objects.update(dt=acc)

        return render(request, 'dtresults.html', {'msg': acc})

    else:
        return render(request, 'admin.html')





def featureres(request):
    if "adminid" in request.session:
        plt.clf()
        performance = []
        row = graph.objects.all()
        for r in row:
            performance.append(r.naive)
            performance.append(r.nn)
            performance.append(r.svm)
            performance.append(r.dt)
            performance.append(r.cnn)
        objects = ('Naive Bayes', 'Neural Network', 'SVM','DT','CNN')
        y_pos = np.arange(len(objects))
        print(performance)
        plt.bar(y_pos, performance, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('Accuracy %')
        plt.title('Performance Algorithms')
        plt.savefig('g2.jpg', dpi=200)
        im = Image.open(r"g2.jpg")
        im.show()

    return render(request, 'featureres.html', {'data': row})


def prediction(request):
    if "useremail" in request.session:
        return render(request, 'usearch.html')
    else:
        return redirect('userlogout')








def getprediction(request):
    url = request.POST['url']
    u = URLCheck()
    res = u.validation(url)
    if res == True:
        pass
    else:
        return render(request, 'search.html', {'msg': "Enter Valid URL"})
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

    if float(res) > 0:
        m = 'Legitimate Website'
    else:
        m = 'Phishing Website'

    return render(request, 'usearch2.html', {'msg': m, 'url': url})
# return render(request, 'usearch2.html')	


# Create your views here. naiveprediction


