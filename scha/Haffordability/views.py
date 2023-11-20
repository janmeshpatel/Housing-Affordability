from django.shortcuts import render, HttpResponse



# import Librarytr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor





# Create your views here.

def home(request):
    return render(request, 'home.html')


def index(request):

    return render(request, 'index.html')


def result(request):

    KNNprice =""
    DTprice = ""
    RFRprice = ""
    LRprice = ""
    SVRprice = ""
    
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

    
    print("hello")
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # train test data split into 30 70 ration
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.30)

        # creating Linear Regression Model
    model = LinearRegression()
    model.fit(X_train, Y_train)
        
    LRpredictions = model.predict(np.array([var1,var2,var3,var4,var5, var6,n1,n2,n3,n4,n5]).reshape(1,-1))
    LRpredictions = round(LRpredictions[0])
    LRprice = "The Predicted price is $"+str(LRpredictions)
    print(LRprice)

    
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # Split the data into training and testing sets
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

    # Create a Random Forest Regressor model
    rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)

    # Train the model on the training set
    rf_regressor.fit(X_train, Y_train.ravel())

    # Make predictions on the test set
    RFRprediction = rf_regressor.predict(np.array([var1,var2,var3,var4,var5, var6,n1,n2,n3,n4,n5]).reshape(1,-1))
    RFRprediction = round(RFRprediction[0])
    RFRprice = "The Predicted price is $"+str(RFRprediction)
    print(RFRprice)
        


    
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # Create a Support Vector Regressor model
    #-svr_regressor = SVR(kernel='linear', C=100)

    # Split the data into training and testing sets
    #-X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

    # Train the model on the training set
    #-svr_regressor.fit(X_train, Y_train.ravel())

    # Make predictions on the test set
    #-SVRprediction = svr_regressor.predict(np.array([var1,var2,var3,var4,var5, var6,n1,n2,n3,n4,n5]).reshape(1,-1))
    #SVRprediction = round(SVRprediction[0])
    #-SVRprice = "The Predicted price is $"+str(SVRprediction)
    #-print(SVRprice)

    
    #  - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    # Split the data into training and testing sets
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    # Create a Decision Tree model
    tree_regressor = DecisionTreeRegressor(max_depth=3)

    # Train the model on the training set
    tree_regressor.fit(X_train, Y_train)

    # Make predictions on the test set
    DTprediction = tree_regressor.predict(np.array([var1,var2,var3,var4,var5, var6,n1,n2,n3,n4,n5]).reshape(1,-1))
    DTprediction = round(DTprediction[0])
    DTprice = "The Predicted price is $"+str(DTprediction)
    print(DTprice)


    
    #  - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    # Create a KNN Model

    # Split the data into training and testing sets
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    # Assuming X_train is a DataFrame
    # Convert it to a NumPy array before applying ravel()
    X_train_array = X_train.values.ravel()

    # Create a k-Nearest Neighbors Regressor model
    knn_regressor = KNeighborsRegressor(n_neighbors=3)  # You can adjust the n_neighbors parameter as needed

    # Train the model on the training set
    knn_regressor.fit(X_train, Y_train)

    # Make predictions on the test set
    KNNprediction = knn_regressor.predict(X_test)  
    KNNprediction = round(KNNprediction[0])
    KNNprice = "The Predicted price is $"+str(KNNprediction)
    print(KNNprice)


    return render(request, 'index.html', {"LRresult" : LRprice, "RFRresult" : RFRprice, "SVMResult" : SVRprice, "DTResult" : DTprice, "KNNResult" : KNNprice})

