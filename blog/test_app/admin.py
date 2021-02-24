from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['author','title','text','create_date','publish_date']