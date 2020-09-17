from django.shortcuts import render
import numpy as np
import pandas as pd
#from django.http import HttpResponse\
from sklearn.linear_model import  LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
# Create your views here.


def home(request):
    return render(request,"index.html")

def predictValue(request):
    Value={}
    if(request.method =="POST"):
        dataset=pd.read_csv('templates/Social_Network_Ads.csv')
        X=dataset.iloc[:,:-1].values
        y=dataset.iloc[:,-1].values
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)
        sc=StandardScaler()
        X_train = sc.fit_transform(X_train)
        X_test = sc.transform(X_test)
        classifier = LogisticRegression(random_state = 0)
        classifier.fit(X_train, y_train)
        age_Value=int(request.POST.get('ageValue'))
        salary_Value=int(request.POST.get('salaryValue'))
        print("value is")
        #print(classifier.predict(sc.transform([[30,87000]])))
        estimated=classifier.predict(sc.transform([[age_Value,salary_Value]]))
        Value={'estimated':estimated}
        return render(request,"index.html",Value)