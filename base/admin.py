from django.contrib import admin

from base.models import Language, PackageRequest


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug',)
    list_display_links = list_display


class PackageRequestAdmin(admin.ModelAdmin):
    pass


admin.site.register(Language, LanguageAdmin)
admin.site.register(PackageRequest, PackageRequestAdmin)
