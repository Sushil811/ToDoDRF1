from django.contrib import admin
from .models import ToDoItem, Tag

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(ToDoItem)
class ToDoItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp', 'due_date', 'status')
    list_filter = ('status', 'due_date', 'tags')
    search_fields = ('title', 'description')
    readonly_fields = ('timestamp',)
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'due_date', 'status')
        }),
        ('Tags', {
            'fields': ('tags',)
        }),
        ('Timestamp', {
            'fields': ('timestamp',)
        }),
    )
