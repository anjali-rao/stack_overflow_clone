from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required

from .models import Question

@login_required
def ask_question(request):
    return render(request, 'ask_question.html')

@login_required
def add_question(request):
    title = request.POST.get('title', '')
    description = request.POST.get('description', '')
    tags = request.POST.get('tags', '')

    if title and description and tags:
        question = Question.objects.create(
            title=title,
            body=description,
            _tags=tags,
            user=request.user
        )

        return JsonResponse(dict(success=True, message="Question created"))

    return JsonResponse(dict(success=False, message="failed to create"))
