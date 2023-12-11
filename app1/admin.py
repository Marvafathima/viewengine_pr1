from django.contrib import admin
from .models import Student
from .models import Products



class StudentAdmin(admin.ModelAdmin):
    list_display=('name','class_name','score')

admin.site.register(Student,StudentAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display=('name','price','stock','image')

admin.site.register(Products,ProductAdmin)

