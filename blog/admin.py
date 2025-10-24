from django.contrib import admin
from .models import BlogPost

# Register your models here.

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['id', 'content_preview', 'created_at']
    list_filter = ['created_at']
    search_fields = ['content']
    
    def content_preview(self, obj):
        return obj.content[:50]
    content_preview.short_description = 'Content'
