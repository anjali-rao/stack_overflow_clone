from userprofile import views

from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.login_page),
    url(r'^login_user', views.login_user)
]
