# Create your views here.
from django.shortcuts import render

def get_index(request):
    return render(request, 'entry/index.html', {})