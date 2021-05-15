from django.contrib import admin

# Register your models here.
from .models import Book,Gift

admin.site.register(Book)
admin.site.register(Gift)