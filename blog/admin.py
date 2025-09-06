from django.contrib import admin
from .models import Post, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "status", "published_at")
    list_filter = ("status", "category", "tags")
    search_fields = ("title", "content", "tags")
    prepopulated_fields = {"slug": ("title",)}