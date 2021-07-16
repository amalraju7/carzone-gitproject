from django.contrib import admin
from .models import Car , Category , Brand , Cars , Chat
from django.utils.html import format_html

# Register your models here.

class CarAdmins(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="250" style="border-radius: 50px" />'.format(object.car_photo.url))

    thumbnail.short_description="Photo";
    list_display = ('id','user','car_title','color','thumbnail','state','district','city','brand','category','model','year','condition','price','description','features','engine','transmission','interior','km_driven','doors','passengers','mileage','fuel_type','no_of_owners','is_featured','created_date')
    list_editable = ('is_featured',)
    search_fields= ('id','car_title','city','fuel_type')
    list_filter = ('brand','category','year')

class BrandAdmin(admin.ModelAdmin):
    list_display=('id','name','description')
    search_fields= ('name','description')

class CategoryAdmin(admin.ModelAdmin):
    list_display=('id','name','description')
    search_fields= ('name','description')


admin.site.register(Cars, CarAdmins)

admin.site.register(Category,CategoryAdmin)
admin.site.register(Brand,BrandAdmin)
