from django.http.response import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

def login_page(request):
    return render(request, "login.html")

def home(request):
    pass

def login_user(request):
    #import pdb; pdb.set_trace()
    #take user name and login, create new if does not exist
    username = request.POST.get("username", '')

    user = User.objects.filter(username=username).first()
    if not user:
        resp = dict(result="invalid credentials", success=False)
        return JsonResponse(resp)

    auth_user = authenticate(request, username)
    login(request, auth_user)
    resp = dict(result="logged in", success=true)
    return JsonResponse(resp)

def display_profile():
    pass

