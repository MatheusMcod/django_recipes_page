from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'recipes/pages/home.html')

def recipes(request, id):
    return render(request, 'recipes/pages/recipeView.html', context={
        'is_detail_text': True
    })

