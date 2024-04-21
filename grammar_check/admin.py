from django.contrib import admin
from .models import Sentence

class SentenceAdmin(admin.ModelAdmin):
    list_display = ('text', 'improved_text')
    list_filter = ('improved_text',)
    search_fields = ('text', 'improved_text')
    list_per_page = 20

admin.site.register(Sentence, SentenceAdmin)
