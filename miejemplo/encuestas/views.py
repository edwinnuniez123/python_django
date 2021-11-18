from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Question
from django.http import Http404
from django.shortcuts import get_object_or_404, render


def index(request):
    #return HttpResponse("Hola Mundo. Tu estas en el indice de la encuesta")
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('encuestas/index.html')
    context = { 
    	'request': request, 
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context))

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'encuestas/detail.html', {'question': question})

def results(request, question_id):
    response = "Tu estas viendo los resultados de la pregunta %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Tu estas votando sobre pregunta %s." % question_id)