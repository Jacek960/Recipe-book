from django.urls import path

from jedzonko.views import IndexView, RecipeListView, DashboardView, RecipeCreateView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('recipe/list', RecipeListView.as_view(), name='recipe_list'),
    path('main', DashboardView.as_view(), name='dashbord'),
    path('recipe/add/', RecipeCreateView.as_view(), name='ad_recipe'),



]