from django.db import models
from datetime import date


class Author(models.Model):

    name = models.CharField(
        max_length=250,
        db_index=True
        )
    email = models.EmailField(
        'Email',
        unique=True
        )
    created_at = models.DateTimeField(
        'Created time',
        auto_now_add=True
        )

    def __str__(self) -> str:
        return self.name


class Book(models.Model):

    title = models.CharField(
        'Book Title',
        max_length=250,
        db_index=True
        )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        verbose_name='Author',
        )
    value = models.BigIntegerField(
        'Value',
    )
    quantity = models.IntegerField(
        'Numbers of books'
    )
    date_published = models.DateField(
        'Publish Date',
        default=date.today
    )
    genre = models.CharField(
        'Genre',
        )
    updated_at = models.DateField(
        'Last Update Date',
        auto_now=True,
    )
    created_at = models.DateField(
        'Created Time',
        auto_now_add=True
    )

    def __str__(self) -> str:
        return f"{self.title} - {self.author}"
    
    def details(self) -> str:
        return f"Price: {self.value}, Published at: {self.date_published}, Quantity: {self.quantity}"

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
