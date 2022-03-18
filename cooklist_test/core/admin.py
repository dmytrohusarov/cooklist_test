from .models import Recipe, Ingredients
from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from import_export import resources


class RecipeResource(resources.ModelResource):
    class Meta:
        model = Recipe
        fields = ('id', 'recipe_data')


class RecipeAdmin(ImportExportModelAdmin):
    resource_class = RecipeResource
    list_display = ('id', 'recipe_data', 'num_ingredients')


class IngredientsAdmin(admin.ModelAdmin):
    model = Ingredients
    list_display = ('text',)


admin.site.register(Ingredients, IngredientsAdmin)

admin.site.register(Recipe, RecipeAdmin)
