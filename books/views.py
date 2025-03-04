from django.urls import reverse_lazy
from django.views import generic
from .models import Book


class BookListView(generic.ListView):
    model = Book
    template_name = 'home.html'
    context_object_name = 'books'


class BookDetailView(generic.DeleteView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'


class BookCreateView(generic.CreateView):
    model = Book
    template_name = 'books/book_create.html'
    fields = ('title', 'author', 'description', 'price', 'cover')


class BookUpdateView(generic.UpdateView):
    model = Book
    fields = ('title', 'author', 'description', 'price', 'cover')
    template_name = 'books/book_create.html'

class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('home')
