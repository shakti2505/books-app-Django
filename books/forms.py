from django import forms

from .models import Books

class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['book_title','book_author', 'book_desc', 'book_price','book_rating','book_image']


