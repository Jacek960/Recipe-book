from django.contrib import admin

# Register your models here.
from jedzonko.models import Receipe, Ingredients, Plan, Dayname, Mealname, Recipeplan

admin.site.register(Receipe)
admin.site.register(Ingredients)
admin.site.register(Plan)
admin.site.register(Dayname)
admin.site.register(Mealname)
# admin.site.register(Recipeplan)

# def mealnames(recipeplan):
#     return [meal_name for meal_name in recipeplan.meal_name.all()]

@admin.register((Recipeplan))
class RecipeplanAdmin(admin.ModelAdmin):
    list_display = ['meal_name','day_name','plan']
