from django.test import TestCase
from django.urls import reverse


class ViewTest(TestCase):

    def test_list_authors(self):
        response = self.client.get(reverse('authors'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'library/authors.html')

    def test_list_book(self):
        response = self.client.get(reverse('books'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'library/books.html')


