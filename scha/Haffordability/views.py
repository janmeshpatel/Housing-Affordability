from django.shortcuts import render, HttpResponse



# import Librarytr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics



# Create your views here.

def home(request):
    return render(request, 'home.html')


def index(request):

    return render(request, 'index.html')


def result(request):

    data = pd.read_csv(r'C:\Users\Janmesh\OneDrive - Saint Peters University\Desktop\Project\scha\Ml_model\California.csv')

    data = data.drop(['longitude'], axis=1)
    data = data.drop(['latitude'], axis =1)

    data.dropna(inplace=True)

    ocean = pd.get_dummies(data.ocean_proximity).astype(int)
    data = data.join(ocean)
    data = data.drop(['ocean_proximity'], axis=1)

    # train test split
    X = data.drop(['median_house_value'], axis=1)
    Y = data['median_house_value']


    # train test data split into 30 70 ration
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.30)

    # creating model
    model = LinearRegression()
    model.fit(X_train, Y_train)

    var1 = float(request.POST['i1'])
    var2 = float(request.POST['i2'])
    var3 = float(request.POST['i3'])
    var4 = float(request.POST['i4'])
    var5 = float(request.POST['i5'])
    var6 = float(request.POST['i6'])
    var7 = request.POST['i7']

    if (var7=='n1'):
        n1=1
        n2=0
        n3=0
        n4=0
        n5=0
    elif (var7=='n2'):
        n1=0
        n2=1
        n3=0
        n4=0
        n5=0
    elif (var7=='n3'):
        n1=0
        n2=0
        n3=1
        n4=0
        n5=0
    elif (var7=='n4'):
        n1=0
        n2=0
        n3=0
        n4=1
        n5=0
    elif (var7=='n5'):
        n1=0
        n2=0
        n3=0
        n4=0
        n5=1
    

    

    print(var1)
    print(var2)
    print(var3)
    print(var4)
    print(var5)
    print(var6)
    print(n1)
    print(n2)
    print(n3)
    print(n4)
    print(n5)
    
    predictions = model.predict(np.array([var1,var2,var3,var4,var5, var6,n1,n2,n3,n4,n5]).reshape(1,-1))

    predictions = round(predictions[0])

    price = "The Predicted price is $"+str(predictions)

    return render(request, 'index.html', {"result2" : price})
