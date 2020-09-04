from django.contrib import admin

from .models import UuId, Formulary, ContentLink


class UuIdAdmin(admin.ModelAdmin):
    pass


class FormularyAdmin(admin.ModelAdmin):
    pass


class ContentLinkAdmin(admin.ModelAdmin):
    pass


admin.site.register(UuId, UuIdAdmin)
admin.site.register(Formulary, FormularyAdmin)
admin.site.register(ContentLink, ContentLinkAdmin)
