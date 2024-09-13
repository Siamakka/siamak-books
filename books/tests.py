from django.test import TestCase
from django.urls import reverse
from .models import Book, Author, Genre
from django.utils import timezone
from datetime import timedelta

class BookModelTests(TestCase):
    def setUp(self):
        # Setup data for tests
        self.author = Author.objects.create(name='Test Author')
        self.genre = Genre.objects.create(name='Test Genre')
        self.book = Book.objects.create(
            title='Test Book',
            author=self.author,
            genre=self.genre,
            price=29.99,
            date_published=timezone.now().date()
        )

    def test_book_creation(self):
        # Test book creation
        self.assertEqual(self.book.title, 'Test Book')
        self.assertEqual(self.book.author.name, 'Test Author')
        self.assertEqual(self.book.genre.name, 'Test Genre')
        self.assertEqual(self.book.price, 29.99)
        self.assertEqual(self.book.date_published, timezone.now().date())

    def test_book_update(self):
        # Test updating book
        self.book.title = 'Updated Book Title'
        self.book.save()
        updated_book = Book.objects.get(id=self.book.id)
        self.assertEqual(updated_book.title, 'Updated Book Title')

    def test_book_deletion(self):
        # Test deleting book
        self.book.delete()
        with self.assertRaises(Book.DoesNotExist):
            Book.objects.get(id=self.book.id)

class BookViewsTests(TestCase):
    def setUp(self):
        # Setup data for views tests
        self.author = Author.objects.create(name='Test Author')
        self.genre = Genre.objects.create(name='Test Genre')
        self.book = Book.objects.create(
            title='Test Book',
            author=self.author,
            genre=self.genre,
            price=29.99,
            date_published=timezone.now().date()
        )

    def test_book_list_view(self):
        # Test the book list view
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Book')

    def test_book_detail_view(self):
        # Test the book detail view
        response = self.client.get(reverse('book_detail', args=[self.book.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Book')

    def test_book_create_view(self):
        # Test creating a new book via the view
        response = self.client.post(reverse('book_create'), {
            'title': 'New Book',
            'author': self.author.id,
            'genre': self.genre.id,
            'price': 19.99,
            'date_published': timezone.now().date()
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful creation
        self.assertTrue(Book.objects.filter(title='New Book').exists())

    def test_book_edit_view(self):
        # Test editing a book via the view
        response = self.client.post(reverse('book_edit', args=[self.book.id]), {
            'title': 'Edited Book Title',
            'author': self.author.id,
            'genre': self.genre.id,
            'price': 39.99,
            'date_published': timezone.now().date()
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful edit
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Edited Book Title')

    def test_book_delete_view(self):
        # Test deleting a book via the view
        response = self.client.post(reverse('book_delete', args=[self.book.id]))
        self.assertEqual(response.status_code, 302)  # Redirect after successful deletion
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())
