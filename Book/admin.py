from django.contrib import admin
from .models import Book,Issue
# Register your models here.
admin.site.register(Book)
admin.site.register(Issue)