from django.contrib import admin
from .models import Post, Comment



class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    list_filter = ['date']
    search_fields = ['title', 'description', 'content']
    date_hierarchy = 'date'
    save_on_top = True


class CommentAdmin(admin.ModelAdmin):
    list_display=['date', 'author']
    list_filter = ['date']
    search_fields = ['author, date, text']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment,CommentAdmin)
