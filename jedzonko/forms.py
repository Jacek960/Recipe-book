from django import forms

from jedzonko.models import Receipe, Plan, Recipeplan, Ingredients


class ReceipeForm(forms.ModelForm):
    class Meta:
        model= Receipe
        fields = ['name','ingredients','description','preparation_time','method_preparation','recipe_image']

class PlanForm(forms.ModelForm):
    class Meta:
        model= Plan
        fields = ['name','description']

class SchedulesMealForm(forms.ModelForm):
    class Meta:
        model = Recipeplan
        fields = ['meal_name','order','day_name','plan','recipe']

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredients
        fields = ['name']
