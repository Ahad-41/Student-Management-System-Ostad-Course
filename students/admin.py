from django.contrib import admin
from .models import Student
 
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'course')
    search_fields = ('name', 'email')
    list_filter = ('course',)
    ordering = ('name',)  # Sort students by name by default
    fieldsets = (
        (None, {
            'fields': ('name', 'email')
        }),
        ('Additional Info', {
            'fields': ('phone_number', 'course'),
            'classes': ('collapse',)  # Collapsible section
        }),
    )