from django.contrib import admin
from todos.models import Todo
from todos.models import *

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Description', {"fields": ["value"]}),
        ("Checking", {"fields": ["checked"]}),
    ]
    list_display = ['value', 'checked']
    
    list_filter = ["checked"]
  
    search_fields = ["value"]


admin.site.register(Todo, TodoAdmin)

