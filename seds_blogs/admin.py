from django.contrib import admin

# Register your models here.
from .models import blog,categories,Trending_blog,video_categories,vlog,vlog_trending,Astrophotography_trending,Astrophotography,categories_Astrophotography


class categories_show(admin.ModelAdmin):
    list_display=[
    'categories',

    ]
    search_fields=['categories']
    list_filter=["categories"]

class blog_show(admin.ModelAdmin):
    list_display=[
    'title',
    'categories',
    ]
    search_fields=['title',]
    list_filter=["categories"]

class Trending_blog_show(admin.ModelAdmin):
    list_display=[
        'title',
        'author',
                 ]
    list_filter=["author"]

class video_categories_show(admin.ModelAdmin):
    list_display=[
    'video_categories',
    ]
class vlog_show(admin.ModelAdmin):
    list_display=[
    'title',
    'video_categories'
    ]

class vlog_trending_show(admin.ModelAdmin):
    list_display=[
    'title',
    ]

class Astrophotography_show(admin.ModelAdmin):
    list_display=[
    'title',
    'categories',
    'date'
    ]
    list_filter=[
    'title',
    'categories'
    ]

admin.site.register(categories,categories_show)
admin.site.register(blog,blog_show)
admin.site.register(Trending_blog,Trending_blog_show)
admin.site.register(video_categories,video_categories_show)
admin.site.register(vlog,vlog_show)
admin.site.register(vlog_trending,vlog_trending_show)
admin.site.register(Astrophotography_trending)
admin.site.register(Astrophotography,Astrophotography_show)
admin.site.register(categories_Astrophotography)
