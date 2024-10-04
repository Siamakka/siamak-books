from rest_framework import viewsets
from books.serializers import UserSerializer
from django.contrib.auth.models import User

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer