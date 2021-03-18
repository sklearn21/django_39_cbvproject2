from django.shortcuts import render
from django.views.generic.list import ListView
from testapp.models import Book

# Create your views here.


# def info_view(request):
#     books = Book.objects.all()
#     return render(request, 'testapp/info.html', {'books': books})


class BookListView(ListView):
    model = Book
    template_name = 'testapp/books.html'
    context_object_name = 'list_of_books'
    # default template: book_list.html
    # default context object: book_list
