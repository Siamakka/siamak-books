from rest_framework import viewsets
from books.serializers import UserSerializer, BookSerializer
from django.contrib.auth.models import User
from .models import Book

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer