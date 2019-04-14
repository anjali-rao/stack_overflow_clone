from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def ask_question(request):
    return render(request, "ask_question.html")

def add_question():
    pass
