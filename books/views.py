from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from .models import Book
from .forms import BookForm
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Book
from .forms import BookForm 
from .forms import AuthorForm
from .forms import SearchForm

def home(request):
    return render(request, 'home.html')


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


def book_create(request):
    form = BookForm()
    if request.method == 'GET':
        return render(request, 'add_book.html', {'form': form})
    
    form = BookForm(request.POST)
    if form.is_valid():
        form.save(commit=True)
        return HttpResponseRedirect(reverse('books:book_list'))
    else:
        return render(request, 'add_book.html', {'form': form})
    
def author_list(request):
    author_list = Book.objects.all()
    return render(request, 'authors_list.html', {'authors': author_list})

    
def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    form = BookForm(instance=book)
    if request.method == 'GET':
        return render(request, 'edit_book.html', {'form': form, 'book_id': book_id})
    
    form = BookForm(request.POST, instance=book)
    if form.is_valid():
        form.save(commit=True)
        return HttpResponseRedirect(reverse('books:book_list'))
    else:
        return render(request, "edit_book.html", {"form": form, "book_id": book_id})
    
def edit_author(request, author_id):
    author = Book.objects.get(id=author)
    form = AuthorForm(instance=author)
    if request.method == "GET":
        return render(request, "edit_author.html", {"form": form, "author_id": author})

    form = AuthorForm(request.POST, instance=author)
    if form.is_valid():
        form.save(commit=True)
        return HttpResponseRedirect(reverse("books:author_list"))
    else:
        return render(request, "edit_author.html", {"form": form, "author_id": author})
    
def add_author(request):
    form = AuthorForm()
    if request.method == 'GET':
        return render(request, 'add_author.html', {'form': form})
    
    form = AuthorForm(request.POST)
    if form.is_valid():
        form.save(commit=True)
        return HttpResponseRedirect(reverse('books:authors_list'))
    else:
        return render(request, 'add_author.html', {'form': form})


def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return HttpResponseRedirect(reverse("books:book_list"))


def filter_books(request):
    form = SearchForm(request.POST)
    if form.is_valid():
        search_text = form.cleaned_data.get("search_text")
        published_date_min = form.cleaned_data.get("published_date_min")
        published_date_max = form.cleaned_data.get("published_date_max")
        min_value = form.cleaned_data.get("min_value")
        max_value = form.cleaned_data.get("max_value")

        books = Book.objects.all()

        if search_text:
            books = books.filter(title__icontains=search_text) or books.filter(author__icontains=search_text)
        if published_date_min:
            books = books.filter(published_at__gte=published_date_min)
        if published_date_max:
            books = books.filter(published_at__lte=published_date_max)
        if min_value:
            books = books.filter(price__gte=min_value)
        if max_value:
            books = books.filter(price__lte=max_value)

        return render(request, "search.html", {"books": books, "form": form})
    else:
        return render(request, "search.html", {"form": form})
    
def books_of_author(request, author_name, country):
    books = Book.objects.filter(author=author_name, author_country=country)
    return render(request, "books_of_author.html", {'books': books, 'author_name': author_name, 'country': country})