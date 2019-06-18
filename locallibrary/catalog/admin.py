from django.contrib import admin
from catalog.models import Author, Book, BookInstance, Genre
# Register your models here.

admin.site.register(Book)
admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Author)