# books_webapp/books/forms.py
from django import forms
from .models import Book, Author, Genre

from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'date_published', 'genre', 'price']
        widgets = {
            'date_published': forms.DateInput(attrs={'type': 'date'}),
            'author': forms.TextInput(attrs={'placeholder': 'Enter author name'}),
            'genre': forms.TextInput(attrs={'placeholder': 'Enter genre'}),
        }

    def clean_author(self):
        author_name = self.cleaned_data.get('author')
        if author_name:
            # Handle creating or fetching the author from the database
            author, created = Author.objects.get_or_create(name=author_name)
            return author
        return None

    def clean_genre(self):
        genre_name = self.cleaned_data.get('genre')
        if genre_name:
            # Handle creating or fetching the genre from the database
            genre, created = Genre.objects.get_or_create(name=genre_name)
            return genre
        return None
