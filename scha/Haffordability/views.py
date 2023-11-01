from django.shortcuts import render, HttpResponse



#import library for implement Models
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import adfuller
from sklearn.metrics import mean_squared_error


# Create your views here.

def index(request):
    
    context = {
            'variable' : 'hello Smart City'
        }
    return render(request, 'index.html', context)

def about(request):
    return HttpResponse("this is about")

def services(request):
    return HttpResponse("this is services")