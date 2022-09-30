from django.urls import path
from .views import Question, Choice

app_name = 'polls'

urlpatterns = [ 
    path('question/', Question.as_view(), name='question'),
    path('choice/', Choice.as_view()),
]