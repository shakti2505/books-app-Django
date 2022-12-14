from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Books(models.Model):
    # associating the pertuculer user with the post he created 
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    book_title = models.CharField(max_length=100)
    book_author = models.CharField(max_length=100, default='')
    book_desc = models.CharField(max_length=200)
    book_price  = models.IntegerField()
    book_rating = models.FloatField()
    book_image = models.CharField(max_length=500, default="https://parallel.cymru/wp-content/uploads/Generic-Book-Placeholder-icon-300x300.png")

    def __str__(self):
        return self.book_title

# this function will redirect the user to the detail page after adding the post
    def get_absolute_url(self):
        return reverse("books:detail", kwargs={"pk": self.pk})
    








