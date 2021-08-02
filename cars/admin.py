from django.contrib import admin
from .models import Car
from django.utils.html import format_html

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="80" style ="border-radius:50px" />'.format(object.car_photo.url))
    thumbnail.short_description = "Car Image"
    list_display = ("id","car_title","thumbnail","state","city","color","model","year","body_style","fuel_type","price","is_featured","status")
    list_display_links=("id","car_title")
    list_editable=("is_featured","status","price",)
    search_fields=("id","car_title","city","model","year","body_style","fuel_type",)
    list_filter=("city","fuel_type","color","is_featured","year",)
    

admin.site.register(Car,CarAdmin)