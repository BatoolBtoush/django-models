from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Snack(models.Model):
    name = models.CharField(max_length=64)
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField()
    calories = models.IntegerField()
    sodium = models.IntegerField()
    fat = models.IntegerField()
    carbs = models.IntegerField()
    protein = models.IntegerField()
    

    def __str__(self):
        return self.name
