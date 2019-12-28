from django.urls import path
from django.conf.urls import url


from .import views


urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<str:slug>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<str:slug>', views.AuthorDetailView.as_view(), name='author-detail'),
]