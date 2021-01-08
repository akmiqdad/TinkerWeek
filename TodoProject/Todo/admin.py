from django.contrib import admin
from .models import Todo

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date_added', 'is_completed')
    search_fields = ('title', 'description')


    class Meta:
        model = Todo

admin.site.register(Todo, TodoAdmin) 