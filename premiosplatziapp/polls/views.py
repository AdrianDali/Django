from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question,Choice
from django.urls import reverse 
#las vistas siempre reciben un request y devuelven un HttpResponse 
def index(request):
    latest_question_list = Question.objects.all()

    return render(request, "polls/index.html", {"latest_question_list": latest_question_list})
    
def detail(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    return HttpResponse("Estas viendo los resultados de la pregunta numero %s." % question_id)

def vote(request,  question_id):
    question = get_object_or_404(Question, pk=question_id)
    try: 
        #intentamos obtener la opcion seleccionada
        selected_choice = question.choice_set.get(pk = request.POST["choice"])

    except(KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "No seleccionaste una opcion",
        })
    #si todo salio bien
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))