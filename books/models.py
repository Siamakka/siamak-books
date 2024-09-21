from django.db import models
from datetime import date


class Book(models.Model):

    title = models.CharField(
        'Book Title',
        max_length=250,
        db_index=True
        )
    author = models.CharField(
        'Author',
        max_length=250,
        )
    author_country = models.CharField(
        'Country',
        max_length=100,
        null=True,
        blank=True,
    )
    value = models.BigIntegerField(
        'Value',
        default=0
    )
    quantity = models.IntegerField(
        'Numbers of books',
        default=1
    )
    date_published = models.DateField(
        'Publish Date',
        default=date.today
    )
    genre = models.CharField(
        'Genre',
        max_length=250
        )
    updated_at = models.DateField(
        'Last Update Date',
        auto_now=True,
    )
    created_at = models.DateField(
        'Created Time',
        default=date.today
    )

    def __str__(self) -> str:
        return f"{self.title} - {self.author}"
    
    def details(self) -> str:
        return f"Price: {self.value}, Published at: {self.date_published}, Quantity: {self.quantity}"