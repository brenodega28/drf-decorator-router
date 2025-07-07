from django.contrib import admin

from . import models


@admin.register(models.MockProduct)
class MockProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "store")


@admin.register(models.MockStore)
class MockStoreAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
