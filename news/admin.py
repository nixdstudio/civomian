from django.contrib import admin
from .models import Post, Mainpost

# Register your models here.
@admin.register(Post,Mainpost)

class PostAdmin(admin.ModelAdmin):
    list_display = ('heading','content')

class PostAdmin(admin.ModelAdmin):
    list_display = ('heading','content')