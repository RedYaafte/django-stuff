from django.contrib import admin

from .models import UuId, Formulary


class UuIdAdmin(admin.ModelAdmin):
    pass


class FormularyAdmin(admin.ModelAdmin):
    pass


admin.site.register(UuId, UuIdAdmin)
admin.site.register(Formulary, FormularyAdmin)
