## Cooklist Backend Developer Take Home Project

### Project Overview

Our Recipe AI has generated a list of 100 Creative AI Recipes and we want to make these available through a GraphQL API.

Create a simple Django project that stores the recipes and their related ingredients and directions that are found in
the file in a database and then makes them available through a GraphQL API. graphene-django is recommended but not
required

You’ll need to define your models, write a function to import the data and store it, and then define the schema to make
the data available through a /graphql endpoint.

Set up a test which returns the data for a single recipe by its ID

Set up a test which returns recipes that have “bacon” in the title or ingredient list

Set up a test which returns recipes that have < 5 ingredients

### Installation

```pip install -r requirements.txt         
python manage.py makemigrations              
python manage.py migrate          
python manage.py createsuperuser   
python manage.py collectstatic      
python manage.py runserver        
```

### Tests

For tests you need to upload test data (`data/100 Creative AI Recipes - cooklist_100_sample_recipes.csv`) through the
admin panel into the system.   
Go to 
`http://127.0.0.1:8000/admin/core/recipe/` - `Import` - Select file and format (csv)   
Methods for graphql:
`http://127.0.0.1:8000/graphql`

1. Get recipes where number od ingredients less or equal 5
```
query{
  getIngrsRecipe(num:5){
    id
    recipeData
  }
  }
```
2. Get recipe by id
```
query{
  recipe(recipeId:2020){
    id
    recipeData
  }
  }
```
3. Get recipes where bacon used in a text
```
query{
  getRecipeText(text:"bacon"){
    id
    recipeData
  }
  }
```




