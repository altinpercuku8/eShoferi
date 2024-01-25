from django.shortcuts import render, HttpResponse
from .models import Quiz
from django.views.generic import ListView
from django.http import JsonResponse
from questions.models import Questions, Anwser
from results.models import Results
# Create your views here.


# Method per te verifikuar metodat Ajax

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


# Fundi i metodes is_ajax


class QuizListView(ListView):
    model = Quiz
    template_name = "main/home.html"


def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request, 'main/single-quiz.html', {'obj': quiz})

def quiz_data_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = []
    for q in quiz.get_question():
        answers = []
        for a in q.get_answer():
            answers.append(a.text)
        questions.append({str(q): answers})
    return JsonResponse({
        'data': questions,
        'time': quiz.time,
    })

def save_quiz_view(request, pk):
    if is_ajax(request=request):
        questions = []
        data = request.POST
        data_ = dict(data.lists())
        # Fshirja e csrf-token-it nga lista
        data_.pop('csrfmiddlewaretoken')
        # iterimi nder pyetjet
        for k in data_.keys():
            print(f"key: {k}")
            question = Questions.objects.get(text=k)
            questions.append(question)
        
        user = request.user
        quiz = Quiz.objects.get(pk=pk)

        score = 0
        multiplier = 100 / quiz.number_of_questions
        results = []
        correct_answer = None

        for q in questions:
            a_selected = request.POST.get(q.text)
            print(f'selected {a_selected}')
            if a_selected != "":
                question_answers = Anwser.objects.filter(question=q)
                for a in question_answers:
                    if a_selected == a.text:
                        if a.correct:
                            score += 1
                            correct_answer = a.text
                    else:
                        if a.correct:
                            correct_answer = a.text
                results.append({str(q):{'correct_answer': correct_answer,'answered':a_selected}})
            else:
                results.append({str(q):"pa pergjigjje"})
        
        score_ = round(score * multiplier)
        Results.objects.create(quiz=quiz, user=user, score=score_)

        if score_ >= quiz.required_score_to_pass:
            return JsonResponse({'passed':True, 'score':score_, 'results':results})
        else:
            return JsonResponse({'passed':False, 'score':score_, 'results':results})


        
        print(data_)
    return JsonResponse({'text':'works'})