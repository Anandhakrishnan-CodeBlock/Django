from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import ListView
from .models import Score


# def index(request):
#    return render(request, 'index.html')

class ScoreListView(ListView):
    model = Score
    template_name = 'index.html'
    context_object_name = 'score'
    ordering = ['-score']

@login_required
def start(request):
    return render(request, 'index.html')
