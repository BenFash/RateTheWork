from django.contrib import admin
from .models import UserContactAdmin


@admin.register(UserContactAdmin)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')
    list_filter = ('name', 'email')
    search_fields = ('name', 'email', 'subject')
