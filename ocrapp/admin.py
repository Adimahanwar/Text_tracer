from django.contrib import admin
from .models import HandwrittenText

@admin.register(HandwrittenText)
class HandwrittenTextAdmin(admin.ModelAdmin):
   # list_display = ('image', 'text')
    list_filter = ('image',)  # Add more fields for filtering if needed
    search_fields = ('text',)  # Add more fields for searching if needed
