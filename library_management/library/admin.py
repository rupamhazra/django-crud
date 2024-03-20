from django.contrib import admin

from library.models import *

# Register your models here.
@admin.register(Book)
class books(admin.ModelAdmin):
    list_display = [field.name for field in Book._meta.fields]
@admin.register(Issue)  
class Issue(admin.ModelAdmin):
    list_display = [field.name for field in Issue._meta.fields]

