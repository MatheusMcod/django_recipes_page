from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    created_at = models.DateTimeField(auto_now_add=True)
