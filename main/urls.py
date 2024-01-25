from django.urls import path
from .views import QuizListView, quiz_view, quiz_data_view, save_quiz_view

urlpatterns = [
    path('', QuizListView.as_view(),name='index'),
    path('quiz/<int:pk>', quiz_view, name='single-quiz'),
    path('quiz/<int:pk>/save/', save_quiz_view, name='save-quiz'),
    path('quiz/<int:pk>/data/', quiz_data_view, name='quiz-data'),
]