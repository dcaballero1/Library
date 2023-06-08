from django.contrib import admin
from .models import Printing, Book, Reader, BookStore

# Register your models here.
admin.site.register(Printing)
admin.site.register(Book)
admin.site.register(Reader)
admin.site.register(BookStore)