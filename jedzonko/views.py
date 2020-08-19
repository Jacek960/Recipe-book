from datetime import datetime

from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from jedzonko.forms import ReceipeForm, PlanForm, SchedulesMealForm, IngredientForm

from jedzonko.models import Receipe, Plan, Dayname, Recipeplan, Ingredients


class IndexView(View):
    def get(self, request):
        return render(request, "jedzonko/index.html", )

class RecipeListView(View):
    def get(self, request):
        recipe_list = Receipe.objects.order_by("votes")
        return render(request, "jedzonko/app-recipes.html", {'recipe_list': recipe_list})

class DashboardView(LoginRequiredMixin,View):
    def get(self,request):
        count_receipe = Receipe.objects.count()
        count_plans = Plan.objects.count()
        plan_exist= Plan.objects.filter(owner=request.user)
        last_plan = plan_exist.last()
        return render(request,'jedzonko/dashboard.html',{'count_receipe':count_receipe,'count_plans':count_plans,'last_plan':last_plan,'plan_exist':plan_exist})



class RecipeCreateView(LoginRequiredMixin,CreateView):
    form_class = ReceipeForm
    success_url = reverse_lazy('recipe_list')
    template_name = 'jedzonko/app-add-recipe.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.owner = self.request.user
        obj.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.request.GET.get('next', self.success_url)


class RecipeUpdate(LoginRequiredMixin,UpdateView):
    model = Receipe
    form_class = ReceipeForm
    template_name = 'jedzonko/app-edit-recipe.html'
    success_url = reverse_lazy('recipe_list')

    def user_passes_test(self, request):
        if request.user.is_authenticated:
            self.object = self.get_object()
            return self.object.owner == request.user
        return False

    def dispatch(self, request, *args, **kwargs):
        if not self.user_passes_test(request):
            return redirect('dashbord')
        return super(RecipeUpdate, self).dispatch(
            request, *args, **kwargs)


class RecipeDeleteView(LoginRequiredMixin, View):
    def get(self, request, id):
        receipe = Receipe.objects.get(pk=id)
        if receipe.owner == request.user:
            receipe_del = Receipe.objects.get(pk=id)
            return render(request, 'jedzonko/app-del-recipe.html', {'receipe_del': receipe_del})
        else:
            return redirect('home')

    def post(self, request, id):
        receipe = Receipe.objects.get(pk=id)
        receipe.delete()
        return redirect('recipe_list')


class PlanListView(LoginRequiredMixin,View):
    def get(self, request):
        plan_list = Plan.objects.filter(owner=request.user).order_by('name')
        return render(request, "jedzonko/app-schedules.html", {'plan_list': plan_list})

# class PlanCreateView(CreateView):
#     form_class = PlanForm
#     success_url = reverse_lazy('plan_list')
#     template_name = 'jedzonko/app-add-schedules.html'
#

class PlanCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = PlanForm()
        return render(request, 'jedzonko/app-add-schedules.html',
                      {'form': form})

    def post(self, request):
        planForm = PlanForm(request.POST, request.FILES)
        if planForm.is_valid():
            plan = planForm.save(commit=False)
            plan.owner = request.user
            plan.save()
        return redirect('plan_list')

class PlanUpdate(LoginRequiredMixin,UpdateView):
    model = Plan
    form_class = PlanForm
    template_name = 'jedzonko/app-edit-schedules.html'
    success_url = reverse_lazy('plan_list')

    def user_passes_test(self, request):
        if request.user.is_authenticated:
            self.object = self.get_object()
            return self.object.owner == request.user
        return False

    def dispatch(self, request, *args, **kwargs):
        if not self.user_passes_test(request):
            return redirect('dashbord')
        return super(PlanUpdate, self).dispatch(
            request, *args, **kwargs)

class PlanDeleteView(LoginRequiredMixin, View):
    def get(self, request, id):
        plan = Plan.objects.get(pk=id)
        if plan.owner == request.user:
            plan_del = Plan.objects.get(pk=id)
            return render(request, 'jedzonko/app-del-plan.html', {'plan_del': plan_del})
        else:
            return redirect('home')

    def post(self, request, id):
        plan = Plan.objects.get(pk=id)
        plan.delete()
        return redirect('plan_list')

class ReceipeDetailView(DetailView):
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
    form_class = SchedulesMealForm
    success_url = reverse_lazy('add-plan-recipe')
    template_name = 'jedzonko/app-schedules-meal-recipe.html'

class SchedulesMealCDelete(DeleteView):
    model = Recipeplan
    template_name = 'jedzonko/app-del-schedules.html'
    success_url = reverse_lazy('dashbord')




# class SchedulesMealCreateView(LoginRequiredMixin, View):
#     def get(self, request):
#         form = SchedulesMealForm(user=request.user)
#         return render(request, 'jedzonko/app-schedules-meal-recipe.html',
#                       {'form': form})
#
#     def post(self, request):
#         plansForm = SchedulesMealForm(request.POST)
#         if plansForm.is_valid():
#             plans = plansForm.save(commit=False)
#             plans.save()
#             plansForm.save_m2m()
#         return redirect('add-plan-recipe')


class IngredientsCreateView(LoginRequiredMixin,CreateView):
    form_class = IngredientForm
    success_url = reverse_lazy('add_ingredient')
    template_name = 'jedzonko/app-add-ingredient.html'

class IngredientUpdate(LoginRequiredMixin,UpdateView):
    model = Ingredients
    form_class = IngredientForm
    template_name = 'jedzonko/apo-edit-ingredients.html'
    success_url = reverse_lazy('ingredient')


class IngredientsListView(ListView):
    paginate_by = 50
    template_name = 'jedzonko/app-ingredients.html'
    model = Ingredients




