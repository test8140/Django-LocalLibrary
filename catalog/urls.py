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

urlpatterns += [
    path('mybooks/', views.loanedBooksByUserListView.as_view(), name='my-borrowed'),
] 


urlpatterns += [
    path('book/<str:slug>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]


urlpatterns += [
    path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
    path('author/<str:slug>/update/', views.AuthorUpdate.as_view(), name='author-update'),
    path('author/<str:slug>/delete/', views.AuthorDelete.as_view(), name='author-delete'),
]  