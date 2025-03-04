from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    cover = models.ImageField(blank=True, upload_to='book_cover/')
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.author}: {self.title}'
    
    def get_absolute_url(self):
        return reverse("book_detail", args={self.id, })
    
class Comment(models.Model):
    text = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='comments' ,on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    recommend = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} At {self.datetime_created}'