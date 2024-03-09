from django.shortcuts import render, reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def select_recipe(request, recipe_key):

    servings = int(request.GET.get('servings', 1))
    template_name = 'calculator/index.html'

    recipe = DATA.get(recipe_key).copy()

    for key, value in recipe.items():
        recipe[key] = value * servings

    context = {
        'recipe': recipe
    }

    return render(request, template_name, context)

def home_view(request):
    template_name = 'calculator/home.html'
    pages = {}

    for recipe_key in DATA.keys():
        pages[recipe_key] = reverse(recipe_key)

    context = {
        'pages': pages
    }

    return render(request, template_name, context)
