from django.contrib import admin
from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "owner",
        "created_at",
        "updated_at",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
    list_filter = ("created_at",)
    ordering = ("-created_at",)
    search_fields = ("title", "owner")
    raw_id_fields = ("owner",)
    prepopulated_fields = {"slug": ("title",)}
