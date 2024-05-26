from django.db import models

# Create your models here.


class Diet(models.Model):

    name = models.TextField()
    email = models.TextField()


class Food(models.Model):

    Name = models.TextField()
    Calories = models.TextField()
    Carbohydrates = models.TextField()
    Proteins = models.TextField()
    Fat = models.TextField()
    Fiber = models.TextField()

