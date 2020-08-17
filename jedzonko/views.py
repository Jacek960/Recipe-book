from datetime import datetime

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from jedzonko.forms import ReceipeForm, PlanForm

from jedzonko.models import Receipe, Plan


class IndexView(View):
    def get(self, request):
        return render(request, "jedzonko/index.html", )

class RecipeListView(View):
    def get(self, request):
        recipe_list = Receipe.objects.order_by("votes")
        return render(request, "jedzonko/app-recipes.html", {'recipe_list': recipe_list})

class DashboardView(View):
    def get(self,request):
        count_receipe = Receipe.objects.count()
        count_plans = Plan.objects.count()
        last_plan= Plan.objects.order_by('-created')[0]
        return render(request,'jedzonko/dashboard.html',{'count_receipe':count_receipe,'count_plans':count_plans,'last_plan':last_plan})



class RecipeCreateView(CreateView):
    form_class = ReceipeForm
    success_url = reverse_lazy('recipe_list')
    template_name = 'jedzonko/app-add-recipe.html'


class PlanListView(View):
    def get(self, request):
        plan_list = Plan.objects.all().order_by('name')
        return render(request, "jedzonko/app-schedules.html", {'plan_list': plan_list})

class PlanCreateView(CreateView):
    form_class = PlanForm
    success_url = reverse_lazy('plan_list')
    template_name = 'jedzonko/app-add-schedules.html'