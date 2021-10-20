from django.contrib import admin
from .models import Profile, Post, City, Comment

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(City)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'body', 'created', 'updated', 'active')
    list_filter = ('active', 'created')
    search_fields = ('post', 'user', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)