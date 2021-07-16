from django.contrib import admin
from .models import Team , Feedback
from django.utils.html import format_html

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.photo.url))

    thumbnail.short_description = 'Photo'

    list_display = ('id', 'thumbnail', 'first_name', 'designation', 'created_date')
    list_display_links = ('id', 'thumbnail', 'first_name',)
    search_fields = ('first_name', 'last_name', 'designation')
    list_filter = ('designation',)

class FeedbackAdmin(admin.ModelAdmin):
    list_display=('id','user','subject','feedback')
    search_fields= ('user','subject','feedback')


admin.site.register(Feedback,FeedbackAdmin)
