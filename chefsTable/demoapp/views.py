from django.http import HttpResponse 
from django.shortcuts import render
from datetime import datetime

def say_hello(request):
    return(HttpResponse("Hello, Django!"))

def home(request):
    return HttpResponse("Welcome to the Chefs' Table!")

def display_date(request):
    return HttpResponse("Today's date is " + str(datetime.now()))