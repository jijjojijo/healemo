from django.contrib import admin

from .models import Coach


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    """Result Admin"""
    pass
