from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

from library.models import Book, Author


def index(request):
    return render(request, 'library/base.html', {})


class Books(ListView):
    model = Book
    context_object_name = 'all_books'
    template_name = 'library/books.html'


class BookDetail(DetailView):
    model = Book
    context_object_name = 'one_book'
    template_name = 'library/book.html'


class BookCreate(CreateView):
    model = Book
    fields = ['title', 'author', 'genre', 'description', 'photo']
    template_name = 'library/create_book.html'


class BookUpdate(UpdateView):
    model = Book
    fields = ['title', 'description', 'photo']
    template_name = 'library/update_book.html'


class BookDelete(DeleteView):
    model = Book
    template_name = 'library/delete_book.html'
    success_url = '/books/'


class Authors(ListView):
    model = Author
    context_object_name = 'all_authors'
    template_name = 'library/authors.html'


class AuthorDetail(DetailView):
    model = Author
    context_object_name = 'one_author'
    template_name = 'library/author.html'


class AuthorCreate(CreateView):
    model = Author
    fields = ['name', 'surname', 'date_of_birthday', 'photo']
    template_name = 'library/create_author.html'


class AuthorUpdate(UpdateView):
    model = Author
    fields = ['name', 'surname', 'date_of_birthday', 'photo']
    template_name = 'library/update_author.html'


class AuthorDelete(DeleteView):
    model = Author
    template_name = 'library/delete_author.html'
    success_url = '/authors/'