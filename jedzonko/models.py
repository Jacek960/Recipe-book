from django.contrib.auth.models import User
from django.db import models


class Ingredients(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Receipe(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.ManyToManyField(Ingredients)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    preparation_time = models.IntegerField()
    votes = models.IntegerField(default=0)
    method_preparation = models.TextField(null=True)
    recipe_image= models.ImageField(upload_to='recipe/',blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Plan(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    recipes = models.ManyToManyField(Receipe, through='Recipeplan')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_recepis(self):
        days = Dayname.objects.order_by('order')
        lst = []
        for day in days:
            lst.append(self.get_meals_for_day(day))
        return lst

    def get_meals_for_day(self, day_id):
        rp = Recipeplan.objects.filter(day_name=day_id, plan=self).order_by('order')
        return rp



class Dayname(models.Model):
    day_name = models.CharField(max_length=16)
    order = models.IntegerField(unique=True)

    def __str__(self):
        return self.day_name


class Mealname(models.Model):
    meal_name = models.CharField(max_length=255)

    def __str__(self):
        return self.meal_name


class Recipeplan(models.Model):
    meal_name = models.CharField(max_length=255)
    order = models.IntegerField()
    day_name = models.ForeignKey(Dayname, on_delete=models.CASCADE, related_name='dayname_recipplan')
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name='plan_recipplan')
    recipe = models.ForeignKey(Receipe, on_delete=models.CASCADE, related_name='recipe_reciplan')

    def __str__(self):
        return f'{self.meal_name}-{self.day_name}'

