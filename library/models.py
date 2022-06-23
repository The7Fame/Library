from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Author(models.Model):
    name = models.CharField(max_length=50, verbose_name='first name')
    surname = models.CharField(max_length=50, verbose_name='second name')
    date_of_birthday = models.DateField(null=True)
    photo = models.FileField(upload_to='authors_photos', blank=True)

    def get_absolute_url(self):
        return reverse('author_detail', args=[str(self.id)])

    def __str__(self):
        return self.name + ' ' + self.surname

    class Meta:
        verbose_name_plural = _('authors')
        verbose_name = _('author')


class Book(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('title of book'))
    description = models.TextField(verbose_name=_('what about book'), null=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    photo = models.FileField(upload_to='books_photos/', blank=True)

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('books')
        verbose_name = _('book')


class Genre(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('genre'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _('genres')
        verbose_name = _('genre')


