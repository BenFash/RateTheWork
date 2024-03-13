from django.contrib import admin
from .models import Work, Category, Rating

# Register your models here.
@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on', 'updated_on')  
    search_fields = ['title', 'content'] 
    list_filter = ['created_on', 'sub_category', 'categories']  

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'work', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('user__username', 'content', 'work__title')
    actions = ['approve_ratings']

    def approve_ratings(self, queryset):
        queryset.update(approved=True)