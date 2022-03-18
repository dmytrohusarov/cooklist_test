from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    recipe_data = models.TextField(default='')
    num_ingredients = models.IntegerField(default=0)


@receiver(post_save, sender=Recipe, dispatch_uid="count ingredients")
def update_ingredients(sender, instance, **kwargs):
    text = instance.recipe_data
    start = text.find('\nIngredients')
    end = text.find('\nDirections:', start)
    if end == -1:
        end = text.find('\nInstructions:', start)

    coor = text[start:end]
    coor = coor.replace("Ingredients\n", "").replace("Ingredients:\n", "")
    lines = coor.split('\n')
    lines = [line for line in lines if line.strip()]
    ingrs = "\n".join(lines)
    ingr = Ingredients.objects.create(
        text=ingrs,
        recipe=instance,
        num_ingredients=sum('\n' in item for item in ingrs) + 1
    )
    ingr.save()


class Ingredients(models.Model):
    text = models.TextField()
    recipe = models.ForeignKey(Recipe, related_name='ingredients', on_delete=models.CASCADE, null=True, blank=True,
                               default=None)
    num_ingredients = models.IntegerField(default=0)
