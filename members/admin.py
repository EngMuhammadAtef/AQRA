from django.contrib import admin
from .models import Member
from .models import Book
from .models import reading

admin.site.register(Member)
admin.site.register(Book)
admin.site.register(reading)

