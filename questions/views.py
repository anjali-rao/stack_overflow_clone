from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Question
from .utils import render_questions

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

        return JsonResponse(dict(success=True, message='Question created'))

    return JsonResponse(dict(success=False, message='failed to create'))

@login_required
def list_user_questions(request):
    user_questions = Question.objects.filter(user=request.user)
    if not user_questions:
        return JsonResponse(dict(success=False))

    return render_questions(request, user_questions, True)

@login_required
def list_community_questions(request):
    community_questions = Question.objects.filter(~Q(user=request.user))
    if not community_questions:
        return JsonResponse(dict(success=False))

    return render_questions(request, community_questions, False)

@login_required
def delete_question(request):
    question_id = request.POST.get("question_id", "")
    question = Question.objects.filter(id=question_id).first()

    if question:
        question.delete()
        return JsonResponse(dict(success=True))

    return JsonResponse(dict(success=False))
