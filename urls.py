"""WebC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [ 
    path('', views.home, name="Welcome"), 
    path('alogin/', views.adminlogindef, name="adminlogindef"), 
    path('ulogin/', views.userlogindef, name="userlogindef"),    
    path('userreg/', views.signupdef, name="signupdef"),    
    path('usignupaction/', views.usignupactiondef, name="usignupactiondef"),
    path('userloginaction/', views.userloginactiondef, name="userloginactiondef"),
    path('userhome/', views.userhomedef, name="userhome"),
    path('userlogout/', views.userlogoutdef, name="userlogout"),
    path('adminloginaction/', views.adminloginactiondef, name="adminloginactiondef"),
    path('adminhome/', views.adminhomedef, name="adminhome"),
    path('alogout/', views.adminlogoutdef, name="adminlogout"),
    path('features/', views.features, name="features"),
    path('naivetest/', views.naivetest, name="naivetest"),
    path('nntest/', views.nntest, name="nntest"),
    path('cnntest/', views.cnntest, name="cnntest"),
    path('dttest/', views.dttest, name="dttest"),
    path('svmtest/', views.svmtest, name="svmtest"),
    
    path('naiveprediction/', views.naiveprediction, name="naiveprediction"),
    path('dtprediction/', views.dtprediction, name="dtprediction"),
    path('nnprediction/', views.nnprediction, name="nnprediction"),
    path('cnnprediction/', views.cnnprediction, name="cnnprediction"),
    path('svmprediction/', views.svmprediction, name="svmprediction"),
    path('featureres/', views.featureres, name="featureres"),

    path('prediction/', views.prediction, name="prediction"),
    path('getprediction/', views.getprediction, name="getprediction"),


]
