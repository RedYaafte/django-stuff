from django.contrib import admin

from .models import UuId


class UuIdAdmin(admin.ModelAdmin):
    pass


admin.site.register(UuId, UuIdAdmin)
