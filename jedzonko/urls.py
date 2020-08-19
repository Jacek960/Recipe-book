from django.urls import path

from jedzonko.views import IndexView, RecipeListView, DashboardView, RecipeCreateView, PlanListView, PlanCreateView, \
    ReceipeDetailView, PlanDetailView, SchedulesMealCreateView, IngredientsCreateView, IngredientsListView, \
    RecipeUpdate, PlanUpdate, IngredientUpdate, RecipeDeleteView, PlanDeleteView, SchedulesMealCDelete

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('recipe/list', RecipeListView.as_view(), name='recipe_list'),
    path('main', DashboardView.as_view(), name='dashbord'),
    path('recipe/add/', RecipeCreateView.as_view(), name='add_recipe'),
    path('plan/list', PlanListView.as_view(), name='plan_list'),
    path('plan/add/', PlanCreateView.as_view(), name='add_plan'),
    path('recipe/<int:pk>/', ReceipeDetailView.as_view(), name='recipe_details'),
    path('plan/<int:id>/', PlanDetailView.as_view(), name='plan_details'),
    path('plan/add-recipe/', SchedulesMealCreateView.as_view(), name='add-plan-recipe'),
    path('ingredient/add/', IngredientsCreateView.as_view(), name='add_ingredient'),
    path('ingredient/', IngredientsListView.as_view(), name='ingredient'),
    path('recipe/modify/<int:pk>/', RecipeUpdate.as_view(), name='update_recipe'),
    path('plan/modify/<int:pk>/', PlanUpdate.as_view(), name='update_plan'),
    path('ingredient/modify/<int:pk>/', IngredientUpdate.as_view(), name='update_ingredient'),
    path('recipe/del/<int:id>/', RecipeDeleteView.as_view(), name='delete_recipe'),
    path('plan/del/<int:id>/', PlanDeleteView.as_view(), name='delete_plan'),
    path('plan_recipe/del/<int:pk>/', SchedulesMealCDelete.as_view(), name='delete_schedules'),


]

