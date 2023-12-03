from django.contrib import admin
from .models import Post2
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    
    list_display = ['title', 'date', 'subTitle', 'date', 'image','images']
    search_fields = ['title']
admin.site.register(Post2, PostAdmin)