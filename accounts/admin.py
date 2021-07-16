from django.contrib import admin
from .models import Package , Cuspack , Card , Packageorder
from django.contrib.auth.models import User
# Register your models here.
class PackageAdmin(admin.ModelAdmin):
    list_display=('id','name','price','cars')
    search_fields= ('id','name','price','cars')


class CuspackAdmin(admin.ModelAdmin):
    inline = [User,]

    list_display=('id','user','no_of_cars','total_cars')
    search_fields= ('id','user','no_of_cars','total_cars')
    def person_name(self,obj):
        return obj.user.email

class CardAdmin(admin.ModelAdmin):

    list_display=('id','user','name','number','expiry')
    search_fields= ('id','user','name','number','expiry')

class PackageorderAdmin(admin.ModelAdmin):

    list_display=('id','user','package','price','status','date')
    search_fields= ('id','package','user','price','status','date')



admin.site.register(Package,PackageAdmin)
admin.site.register(Cuspack,CuspackAdmin)
admin.site.register(Card,CardAdmin)
admin.site.register(Packageorder,PackageorderAdmin)
