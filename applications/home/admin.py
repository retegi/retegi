from django.contrib import admin
from .models import Post, Technology, Comment, Hacked


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ("date_time", "title", "image", "author")
    filter_horizontal = ('technology',)
admin.site.register(Post,PostAdmin)

class TechnologyAdmin(admin.ModelAdmin):
    list_display = ("name","image")
admin.site.register(Technology,TechnologyAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ("content2","post","user")
admin.site.register(Comment,CommentAdmin)

class HackedAdmin(admin.ModelAdmin):
    list_display = ("victim","locality")
admin.site.register(Hacked,HackedAdmin)

