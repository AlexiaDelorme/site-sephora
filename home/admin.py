from django.contrib import admin
from . import models


class SpecialtyAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name'
    )

    ordering = ('id',)


class SubSpecialtyAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name'
    )

    ordering = ('id',)


class ListForSubSpecialtyAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name'
    )

    ordering = ('id',)


admin.site.register(models.Specialty, SpecialtyAdmin)
admin.site.register(models.SubSpecialty, SubSpecialtyAdmin)
admin.site.register(models.ListForSubSpecialty, ListForSubSpecialtyAdmin)