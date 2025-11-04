from django.shortcuts import render
from .models import Book
# Create your views here.
def inventory_pages(request):
    book_list = Book.objects.all()
    return render(request, 'inventory/inventory.html', {'books_list':book_list})