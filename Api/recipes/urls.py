from django.urls import path
from recipes.views import RecipeListAndCreate, RecipeDetailChangeAndDelete

urlpatterns = [
    path('', RecipeListAndCreate.as_view()),
    path('<int:pk>/', RecipeDetailChangeAndDelete.as_view())
]
