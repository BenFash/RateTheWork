from django.contrib import admin
from .models import Work, Category, Rating, Profile


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on', 'updated_on', 'approved', 'user')
    search_fields = ('title', 'content', 'approved', 'user',)
    list_filter = ['created_on',
                   'sub_category', 'categories', 'approved', 'user']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'work', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('user__username', 'content', 'work__title')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_image', 'user_type')
    list_filter = ('user_type',)
    search_fields = ('user__username', 'user_type')

