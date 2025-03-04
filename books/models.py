from django.db import models
from django.urls import reverse

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    cover = models.ImageField(blank=True, upload_to='book_cover/')

    def __str__(self):
        return f'{self.author}: {self.title}'
    
    def get_absolute_url(self):
        return reverse("book_detail", args={self.id, })