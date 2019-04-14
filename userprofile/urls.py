from userprofile import views

from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.home, name="home"),

    url(r'^login$', views.login_page, name="login"),
    url(r'^login_user$', views.login_user, name="login_user"),
    url(r'^signup$', views.signup, name="signup"),
    url(r'^logout$', views.logout_user, name="logout"),
]
