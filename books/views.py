from django.urls import reverse_lazy
from django.views import generic
from .models import Book
from django.shortcuts import get_object_or_404, render
from .forms import CommentForm


class BookListView(generic.ListView):
    model = Book
    template_name = 'home.html'
    context_object_name = 'books'
    paginate_by = 4


# class BookDetailView(generic.DeleteView):
#     model = Book
#     context_object_name = 'book'
#     template_name = 'books/book_detail.html'

def book_detail_view(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = book
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()
            
    else:
        comment_form = CommentForm()

    return render(request, 'books/book_detail.html', {
        'book': book,
        'comments': book.comments.all(),
        'comment_form': comment_form,
    })


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
