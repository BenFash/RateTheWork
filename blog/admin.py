from django.contrib import admin
from .models import Work, Category
# Register your models here.
@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on', 'updated_on')  
    search_fields = ['title', 'content'] 
    list_filter = ['created_on', 'sub_category', 'categories']  

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)