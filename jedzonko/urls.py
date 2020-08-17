from django.urls import path

from jedzonko.views import IndexView, RecipeListView, DashboardView, RecipeCreateView, PlanListView, PlanCreateView, \
    ArticleDetailView, PlanDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('recipe/list', RecipeListView.as_view(), name='recipe_list'),
    path('main', DashboardView.as_view(), name='dashbord'),
    path('recipe/add/', RecipeCreateView.as_view(), name='ad_recipe'),
    path('plan/list', PlanListView.as_view(), name='plan_list'),
    path('plan/add/', PlanCreateView.as_view(), name='ad_plan'),
    path('recipe/<int:pk>/', ArticleDetailView.as_view(), name='recipe_details'),
    path('plan/<int:id>/', PlanDetailView.as_view(), name='plan_details'),



]