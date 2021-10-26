from django.contrib import admin
from .models import Profile, Post, City, Comment

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)

class CityAdmin(admin.ModelAdmin):
  list_display = ['name']
  prepopulated_fields = {'slug': ('name',)}

admin.site.register(City, CityAdmin)