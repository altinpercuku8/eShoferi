from django.urls import path
from .views import QuizListView, quiz_view

urlpatterns = [
    path('', QuizListView.as_view(),name='index'),
    path('quiz/<int:pk>', quiz_view, name='single-quiz'),
]