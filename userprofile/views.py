from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .utils import auth_user

def login_page(request):
    return render(request, "login.html")

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

def login_user(request):
    #take user name and login, create new if does not exist

    username = request.POST.get('username', '')
    resp = auth_user(request, username)

    return JsonResponse(resp)

def logout_user(request):
    logout(request)
    return redirect("login")

@login_required
def home(request):

    context = dict(user=request.user)
    return render(request, "home.html", context);

def display_profile():
    pass
