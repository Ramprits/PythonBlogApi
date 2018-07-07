from django.contrib import admin
from .models import (Post, Category)


class PostModelAdmin(admin.ModelAdmin):

    list_display = ('name', 'title', 'created')


class CategoryModelAdmin(admin.ModelAdmin):

    list_display = ('name', 'created')


admin.site.register(Category, CategoryModelAdmin)
admin.site.register(Post, PostModelAdmin)
