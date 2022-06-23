from django.test import TestCase
from library.models import Author


class AuthorTest(TestCase):

    def test_create_book_no_photo(self):
        book = Author.objects.create(name='Name', surname='Surname')
        self.assertTrue(Author.objects.all().filter(id=1))
        self.assertIn(Author.objects.first().name, 'Name')
        self.assertTrue(Author.objects.all().filter(id=1))

    def test_create_book_photo(self):
        book = Author.objects.create(name='Name', surname='Surname', photo='some photo')
        self.assertTrue(Author.objects.all().filter(id=1))
        self.assertIn(Author.objects.first().name, 'Name')