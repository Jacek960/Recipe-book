from django import forms
from django.forms import ModelMultipleChoiceField, SelectMultiple

from jedzonko.models import Receipe, Plan


class ReceipeForm(forms.ModelForm):
    class Meta:
        model= Receipe
        fields = ['name','ingredients','description','preparation_time','method_preparation','recipe_image']

class PlanForm(forms.ModelForm):
    class Meta:
        model= Plan
        fields = ['name','description']
