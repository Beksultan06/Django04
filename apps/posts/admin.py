from django.contrib import admin
from apps.posts.models import Post, Comment


# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "created", "status", "category"]
    list_filter = ["title", "status", "category"]
    list_editable = ["status"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["post", "name", "created"]