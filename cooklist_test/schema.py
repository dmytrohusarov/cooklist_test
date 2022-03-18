import graphene
from graphene_django import DjangoObjectType

from cooklist_test.core.models import Recipe, Ingredients


class RecipeType(DjangoObjectType):
    num_ingredients = graphene.String(source='num_ingredients')

    class Meta:
        model = Recipe
        fields = ("id", "recipe_data")


class Query(graphene.ObjectType):
    all_recipe = graphene.List(RecipeType)
    recipe = graphene.Field(RecipeType, recipe_id=graphene.Int())
    get_recipe_text = graphene.List(RecipeType, text=graphene.String())
    get_ingrs_recipe = graphene.List(RecipeType, num=graphene.Int())

    def resolve_all_recipe(self, info, **kwargs):
        return Recipe.objects.all()

    def resolve_recipe(self, info, recipe_id):
        return Recipe.objects.get(pk=recipe_id)

    def resolve_get_recipe_text(self, info, text):
        return Recipe.objects.filter(recipe_data__contains=text)

    def resolve_get_ingrs_recipe(self, info, num):
        ingrs = Ingredients.objects.filter(num_ingredients__lte=num)
        return Recipe.objects.filter(ingredients__in=ingrs)


schema = graphene.Schema(query=Query)
