from django.shortcuts import render
import json

def login_page(request):
    return render(request, "login.html")

def home(request):
    pass

def login_user():
    #take user name and login, create new if does not exist
    pass

def display_profile():
    pass

