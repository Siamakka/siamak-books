from django.contrib import admin
from django.contrib import messages
from .models import Book
from django.db.models import F


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

    actions = [
        'add_value',
    ]

    def add_value(self, request, queryset):
        updated_books_count = queryset.update(value=F('value') + 10)
        self.message_user(
            request,
            f'Added value to {updated_books_count} books values',
            messages.SUCCESS,
        )
    add_value.short_description = 'Add 10 to values'