from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView

from recipes.models import Recipe
from recipes.serializers import RecipeSerializer

class RecipeListAndCreate(APIView):
    def get(self, request):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RecipeDetailChangeAndDelete(APIView):
    def get_object(self, pk):
        try:
            return Recipe.objects.get(pk=pk)
        except Recipe.DoesNotExist:
            return NotFound()
    
    def get(self, request, pk):
        recipes = self.get_object(pk)
        serializer = RecipeSerializer(recipes)
        return Response(serializer.data)
    
    def put(self, request, pk):
        recipes = self.get_object(pk)
        serializer = RecipeSerializer(recipes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        recipes = self.get_object(pk)
        recipes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
