from django.contrib import admin

from student.models import *

# Register your models here.
@admin.register(Student)
class Student(admin.ModelAdmin):
    list_display = [field.name for field in Student._meta.fields]
