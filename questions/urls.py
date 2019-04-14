from questions import views

from django.conf.urls import url

urlpatterns = [
    url(r'^ask', views.ask_question, name="ask_question"),
    url(r'^add_question$', views.add_question, name="add_question"),
]
