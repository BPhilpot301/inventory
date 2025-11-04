from django.urls import path
from . import views

urlpatterns = [
    path('inventory/', views.inventory_pages, name='inventory_page'),
    path('add_book/', views.add_book_view, name='add_book'),
    path('edit_book/<int:id>/', views.edit_book_view, name= 'edit_book'),
]