from django.shortcuts import render, HttpResponse
from .models import Quiz
from django.views.generic import ListView
# Create your views here.


class QuizListView(ListView):
    model = Quiz
    template_name = "main/home.html"


def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request, 'main/single-quiz.html', {'obj': quiz})
