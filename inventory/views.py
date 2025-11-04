from django.shortcuts import redirect, render
from .models import Book
from.forms import BookForm


# Create your views here.
def inventory_pages(request):
    book_list = Book.objects.all()
    return render(request, 'inventory/inventory.html', {'books_list':book_list})

def add_book_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory_page')
    else:
        form = BookForm()

    return render(request, 'inventory/add_book.html', {'form':form})

def edit_book_view(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('inventory_page')
    else:
        form = BookForm(instance=book)
    return render(request, 'inventory/edit_book.html', {'form':form})

