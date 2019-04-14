
from django.conf.urls import url

from questions import views

urlpatterns = [
    url(r'^ask', views.ask_question, name='ask_question'),
    url(r'^add_question', views.add_question, name='add_question'),
    url(r'^user_questions', views.list_user_questions, name='user_questions'),
    url(r'^community_questions', views.list_community_questions, name='community_questions'),
    url(r'^delete_question', views.delete_question, name='delete_question'),
]
