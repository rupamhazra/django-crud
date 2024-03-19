from django.contrib import admin

from library.models import *

# Register your models here.
@admin.register(Books)
class books(admin.ModelAdmin):
    list_display = [field.name for field in Books._meta.fields]
@admin.register(Issue)  
class Issue(admin.ModelAdmin):
    list_display = [field.name for field in Issue._meta.fields]

