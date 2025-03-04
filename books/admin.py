from django.contrib import admin
from .models import Book, Comment

# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'book', 'datetime_created', 'is_active', 'recommend')


admin.site.register(Book)
admin.site.register(Comment, CommentAdmin)
