from django.contrib import admin
from .models import Book


# Register your models here.
@admin.register(Book)
class bookAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'author',
        'genre',
        'value',
    ]

    sortable_by = [
        'id',
    ]

    list_filter = [
        'author_country',
    ]

    list_editable = [
        'title',
        'author',
        'value',
        'genre',
    ]

    search_fields = [
        'title',
        'author',
        'value',
        'author_country',
    ]