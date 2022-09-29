from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class Question(View):
    def get(self, request, *args, **kwargs):
        context= {

        }
        return render(request, 'question.html', context)

class Choice(View):
    def get(self, request, *args, **kwargs):
        context= {

        }
        return render(request, 'choice.html', context)