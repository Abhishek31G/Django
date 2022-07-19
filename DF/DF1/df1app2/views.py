from django.shortcuts import render
from .models import Book, Store

# Create your views here.
def view_books(request):
    books = Book.objects.all().prefetch_related('store_set')
    for book in books:
        result = book.store_set.all()
        print(result)
    store = Store.objects.all()
    context = {
        'result': result,
        'books': books,
        'store': store
    }
    return render(request, 'view_books.html', context)