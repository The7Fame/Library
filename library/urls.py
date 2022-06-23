from django.urls import path
from .views import Books, Authors, BookDetail, AuthorDetail, index, \
    BookDelete, BookCreate, BookUpdate, AuthorDelete, AuthorCreate, AuthorUpdate

urlpatterns = [
    path('', index, name='home'),
    path('authors/', Authors.as_view(), name='authors'),
    path('author/<int:pk>/', AuthorDetail.as_view(), name='author_detail'),
    path('author/delete/<int:pk>', AuthorDelete.as_view(), name='delete_author'),
    path('author/create', AuthorCreate.as_view(), name='create_author'),
    path('author/update/<int:pk>', AuthorUpdate.as_view(), name='update_author'),
    path('books/', Books.as_view(), name='books'),
    path('book/<int:pk>/', BookDetail.as_view(), name='book_detail'),
    path('book/delete/<int:pk>', BookDelete.as_view(), name='delete_book'),
    path('book/create', BookCreate.as_view(), name='create_book'),
    path('book/update/<int:pk>', BookUpdate.as_view(), name='update_book'),
]