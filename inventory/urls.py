from django.urls import path
from . import views

urlpatterns = [
    path('inventory/', views.inventory_pages, name='inventory_page')
    
]