from django.contrib import admin
from .models import Profile, Post, City, Comment

# Register your models here.
admin.site.register(Profile)
admin.site.register(Comment)

class CityAdmin(admin.ModelAdmin):
  list_display = ('name', 'country',)
  prepopulated_fields = {'slug': ('name',)}

admin.site.register(City, CityAdmin)


class PostAdmin(admin.ModelAdmin):
  list_display = ('title', 'city',)
  prepopulated_fields = {'slug': ('title', 'city',)}
  
admin.site.register(Post, PostAdmin)