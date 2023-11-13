from django.shortcuts import render, HttpResponse



#import library for implement Models
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



# Create your views here.

def index(request):

    # load datset into data
    #data = pd.read_csv('scha\Dataset\California.csv')
    
    context = {
            'variable' : "hello"
        }
    return render(request, 'index.html', context)

def about(request):
    return HttpResponse("this is about")

def services(request):
    return HttpResponse("this is services")