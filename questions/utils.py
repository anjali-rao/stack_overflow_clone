from django.http.response import JsonResponse
from django.template import loader

def render_questions(request, questions, delete_access):
    '''
    Renders every question into the given template
    along with delete access flag
    '''
    template = loader.get_template('question_card.html')
    context = dict(questions=questions, delete_access=delete_access)
    html = template.render(context, request)

    return JsonResponse(dict(html=html, success=True))


