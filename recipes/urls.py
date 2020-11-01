from django.contrib import admin
from django.urls import path

from recipes.views import home_page_view, create_recipe_view, edit_recipe_view, delete_recipe_view, details_recipe_view

urlpatterns = [
    path('', home_page_view, name='home page'),
    path('create/', create_recipe_view, name='create recipe'),
    path('edit/<int:my_id>/', edit_recipe_view, name='edit recipe'),
    path('delete/<int:my_id>/', delete_recipe_view, name='delete recipe'),
    path('details/<int:my_id>/', details_recipe_view, name='details recipe')
]
