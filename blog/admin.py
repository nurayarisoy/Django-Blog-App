from django.contrib import admin

from blog.models import Comment, Like, Post, PostView

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(PostView)
