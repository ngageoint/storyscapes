from django.contrib import admin
from .models import Theme


class ThemeAdmin(admin.ModelAdmin):
    model = Theme
    list_display = ('name', 'active_theme', 'description')

    def get_readonly_fields(self, request, obj=None):
        if obj is not None and obj.default_theme:
            return ['background_logo', 'primary_logo', 'banner_logo']
        return []


admin.site.register(Theme, ThemeAdmin)
