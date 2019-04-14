from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

def auth_user(request, username):
    user = User.objects.filter(username=username).first()
    if not user:
        _resp = dict(message='Invalid Credentials', success=False)
        return _resp

    authenticate(request=request, username=username)
    login(request, user)
    _resp = dict(result='logged in', success=True)
    return _resp

