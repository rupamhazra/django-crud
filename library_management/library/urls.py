from django.urls import path
from . import views
    
urlpatterns = [
    path('', views.index, name='index'),
    path('books/list/', views.list_books, name='books'),
    path('books/add/', views.add_book, name='books-add'),
    path('books/details/<id>', views.details, name='books-details'),
    path('books/edit/<id>', views.bookEdit, name='books-edit'),
]    