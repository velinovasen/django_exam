from django.shortcuts import render, redirect
from .forms import RecipeForm, DisabledRecipeForm
# Create your views here.
from recipes.models import Recipe


def home_page_view(request):
    if Recipe.objects.all():
        context = {
            "all_recipes": Recipe.objects.all()
        }
        return render(request, 'index.html', context)
    return render(request, 'index.html')


def create_recipe_view(request):
    if request.POST:
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
        return render(request, 'create.html', {"form": RecipeForm()})

    context = {
        "form": RecipeForm()
    }
    return render(request, 'create.html', context)


def edit_recipe_view(request, my_id):
    recipe = Recipe.objects.get(pk=my_id)
    if request.POST:
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home page')
        return render(request, 'edit.html', {"form": RecipeForm(instance=recipe)})
    form = RecipeForm(instance=recipe)
    return render(request, 'edit.html', {"form": form})


def delete_recipe_view(request, my_id):
    recipe = Recipe.objects.get(pk=my_id)
    if request.POST:
        recipe.delete()
        return redirect('home page')
    return render(request, 'delete.html', {"form": DisabledRecipeForm(instance=recipe)})


def details_recipe_view(request, my_id):
    recipe = Recipe.objects.get(pk=my_id)
    ingredients = recipe.ingredients.split(', ')
    context = {
        "recipe": recipe,
        "ingredients": ingredients
    }
    return render(request, 'details.html', context)