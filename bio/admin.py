from django.contrib import admin
from .models import bio_info
# Register your models here.

class bio_info_show(admin.ModelAdmin):
    list_display=[
    'name',
    'batch',
    'dept'
    ]
    search_fields=['name']
    list_filter=['batch']


admin.site.register(bio_info,bio_info_show)
