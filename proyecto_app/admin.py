from django.contrib import admin
from .models import Imprenta, Libro, Lector, Biblioteca

# Register your models here.
admin.site.register(Imprenta)
admin.site.register(Libro)
admin.site.register(Lector)
admin.site.register(Biblioteca)