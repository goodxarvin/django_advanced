from ast import mod
from django.contrib import admin
from .models import Post, Category

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ("id", 'title', 'author', 'category', 'status', 'created_at', 'updated_at', 'published_at')
    list_filter = ('status', 'category', 'author')
    search_fields = ('title', 'content')
    list_editable = ('status', 'category')
    list_per_page = 10
    list_display_links = ('title', 'author')

admin.site.register(Post, PostAdmin)

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ('name',)

    list_per_page = 10
    list_display_links = ('name',)

admin.site.register(Category, CategoryAdmin)