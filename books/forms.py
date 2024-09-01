from django import forms
from .models import Book, Author, Genre


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'authors', 'genres', 'published_date']
