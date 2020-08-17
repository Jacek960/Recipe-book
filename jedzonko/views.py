from datetime import datetime

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView
from jedzonko.forms import ReceipeForm, PlanForm, SchedulesMeal

from jedzonko.models import Receipe, Plan, Dayname, Recipeplan


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

class ArticleDetailView(DetailView):
    model = Receipe
    template_name = 'jedzonko/app-recipe-details.html'
    pk_url_kwarg = 'pk'


class PlanDetailView(View):
    def get(self,request,id):
        plan = Plan.objects.get(id=id)
        days_in_week = Dayname.objects.order_by("order")
        ret_val = []
        for day in days_in_week:
            temp = Recipeplan.objects.filter(day_name_id=day, plan_id=plan).order_by('order')
            ret_val.append(temp)
            return render(request, 'jedzonko/app-details-schedules.html',
                          {'recepi_plan': ret_val, 'plan': plan, 'days_in_week': days_in_week})


class SchedulesMealCreateView(CreateView):
    form_class = SchedulesMeal
    success_url = reverse_lazy('add-plan-recipe')
    template_name = 'jedzonko/app-schedules-meal-recipe.html'

