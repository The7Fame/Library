from library.models import Book, Author, Genre
from django.test import TestCase


class BookTest(TestCase):

    def test_create_book_no_photo(self):
        author = Author.objects.create(name='Name', surname='Surname')
        genge = Genre.objects.create(name='Genre')
        book = Book.objects.create(author=author,
                                   genre=genge,
                                   title='Title',
                                   description='Desr')
        self.assertTrue(Book.objects.all().filter(id=1))
        self.assertIn(Book.objects.first().title, 'Title')

    def test_create_book_photo(self):
        author = Author.objects.create(name='Name', surname='Surname')
        genge = Genre.objects.create(name='Genre')
        book = Book.objects.create(author=author,
                                   genre=genge,
                                   title='Title',
                                   description='Desr',
                                   photo='some photo')
        self.assertTrue(Book.objects.all().filter(id=1))
        self.assertIn(Book.objects.first().title, 'Title')