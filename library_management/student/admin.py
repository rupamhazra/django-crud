from django.contrib import admin

from student.models import *

# Register your models here.
@admin.register(student)
class Student(admin.ModelAdmin):
    list_display = [field.name for field in student._meta.fields]
