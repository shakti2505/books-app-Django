from books.models import Books
from books.api.serializers import BookSerializer
from rest_framework import viewsets

class BookViewSet(viewsets.ModelViewSet):
    queryset= Books.objects.all()
    serializer_class = BookSerializer

    




