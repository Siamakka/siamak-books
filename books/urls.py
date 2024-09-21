from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
    path("", views.home, name="home"),
    path("list/", views.book_list, name="book_list"),
    path("show_authors/", views.author_list, name="author_list"),
    path("author/<str:author_name>/<str:country>/", views.books_of_author, name="books_of_author"),
    path("add_book/", views.book_create, name="add-book"),
    path("edit_book/<int:book_id>/", views.edit_book, name="edit-book"),
    path("delete_book/<int:book_id>/", views.delete_book, name="delete-book"),
    path("search/", views.filter_books, name="search"),
]