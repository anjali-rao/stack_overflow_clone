from django.http.response import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User

from .utils import auth_user

def login_page(request):
    return render(request, "login.html")

def home(request):
    pass

def login_user(request):
    #take user name and login, create new if does not exist

    username = request.POST.get('username', '')
    resp = auth_user(request, username)

    return JsonResponse(resp)

def signup(request):
    #Creates a record for a new user.

    username = request.POST.get('username', '')
    user = User.objects.filter(username=username).first()

    if user:
        resp = dict(message='Username already exists', success=False)
        return JsonResponse(resp)

    user = User.objects.create_user(username=username)
    if not user:
        resp = dict(success=False, result="Signup failed")
        return resp

    resp = auth_user(request, username)

    return JsonResponse(resp)

def display_profile():
    pass
