from django.contrib import admin

from .models import Group


class GroupAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "description")
    search_fields = ("title",)


admin.site.register(Group, GroupAdmin)
