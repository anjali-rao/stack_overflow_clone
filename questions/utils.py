from django.http.response import JsonResponse
from django.template import loader

def render_questions(request, questions, delete_access):

    template = loader.get_template('question_card.html')
    context = dict(questions=questions, delete_access=delete_access)
    html = template.render(context, request)

    return JsonResponse(dict(html=html, success=True))


