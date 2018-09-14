from django.contrib import admin

from base.models import Language, PackageRequest


class LanguageAdmin(admin.ModelAdmin):
    pass


class PackageRequestAdmin(admin.ModelAdmin):
    pass


admin.site.register(Language, LanguageAdmin)
admin.site.register(PackageRequest, PackageRequestAdmin)
