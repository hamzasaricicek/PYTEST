from django.contrib import admin

# Register your models here.
from post.models import post
from post.models import Urunler


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'publishing_date']
    list_display_links = ['publishing_date']
    list_filter = ['publishing_date', 'content']
    search_fields = ['title', 'content']
    list_editable = ['title', 'content']

    class Meta:
        model = post


class UrunlerAdmin(admin.ModelAdmin):
    list_display = ['UrunAdi']

    class Meta:
        model = Urunler


admin.site.register(post, PostAdmin)
