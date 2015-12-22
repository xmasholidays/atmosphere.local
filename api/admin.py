from django.contrib import admin

from .models import Audio, Request

from django.contrib import admin


class AudioAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_background')


class RequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'audio')


admin.site.register(Audio, AudioAdmin)
admin.site.register(Request, RequestAdmin)
