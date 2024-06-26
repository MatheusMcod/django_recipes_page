from recipes.models import Recipe

from rest_framework import serializers

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'description', 'created_at']
        