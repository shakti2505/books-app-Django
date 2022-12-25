from books.models import Books
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Books
        fields = ['id', 'user_name', 'book_title', 'book_author', 'book_desc', 'book_price', 'book_rating','book_image']


        