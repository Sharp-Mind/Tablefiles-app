from django.contrib import admin
from .models import TableFile


@admin.register(TableFile)
class TableFileAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}