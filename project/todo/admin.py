from django.contrib import admin
from todo.models import TodoItem


class TodoItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(TodoItem, TodoItemAdmin)