from django.contrib import admin
from .models import Work, Category
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Work)
class WorkAdmin(SummernoteModelAdmin):
    list_display = ('title', 'created_on', 'updated_on')  
    search_fields = ['title', 'content'] 
    list_filter = ['created_on', 'sub_category', 'categories']  #
    summernote_fields = ('content',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)