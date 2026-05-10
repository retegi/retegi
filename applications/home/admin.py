from django.contrib import admin
from parler.admin import TranslatableAdmin, TranslatableTabularInline
from .models import Post, Technology, Comment, Hacked


@admin.register(Post)
class PostAdmin(TranslatableAdmin):  # ✅ Usa TranslatableAdmin
    list_display = ('title_translated', 'author', 'date_time')
    search_fields = ('translations__title',)
    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'summary', 'author', 'image', 'technology', 'github', 'video')
        }),
    )

    def title_translated(self, obj):
        return obj.safe_translation_getter('title', any_language=True)
    
    title_translated.admin_order_field = 'translations__title'
    title_translated.short_description = 'Title'



class TechnologyAdmin(admin.ModelAdmin):
    list_display = ("name","image")
admin.site.register(Technology,TechnologyAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ("content2","post","user")
admin.site.register(Comment,CommentAdmin)

class HackedAdmin(admin.ModelAdmin):
    list_display = ("victim","locality")
admin.site.register(Hacked,HackedAdmin)

