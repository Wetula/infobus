from django.contrib import admin

from .models import Buses, Routes, Times, Stops


# ModelAdmin objects
class BusesAdmin(admin.ModelAdmin):
    list_filter = ('inorder',)
    ordering = ['busname']
    pass


class RoutesAdmin(admin.ModelAdmin):
    ordering = ['busname', 'stopid']
    pass


class TimesAdmin(admin.ModelAdmin):
    ordering = ['stopid', 'time', 'busname']
    pass


class StopsAdmin(admin.ModelAdmin):
    ordering = ['stopname']
    pass


# Register your models here.

admin.site.register(Buses, BusesAdmin)
admin.site.register(Routes, RoutesAdmin)
admin.site.register(Times, TimesAdmin)
admin.site.register(Stops, StopsAdmin)
