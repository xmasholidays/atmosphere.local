from django.contrib import admin

from .models import Audio, Request

from django.contrib import admin


class AudioAdmin(admin.ModelAdmin):
    pass


class RequestAdmin(admin.ModelAdmin):
    pass


admin.site.register(Audio, AudioAdmin)
admin.site.register(Request, RequestAdmin)
