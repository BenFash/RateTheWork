from django.contrib import admin
from .models import ContactAdmin


@admin.register(ContactAdmin)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'subject', 'message')
    list_filter = ('user',)
    search_fields = ('user__username', 'email', 'subject')
