from django.contrib import admin
from .models import Author, Tag, Quote


# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "fullname", "date_born", "location_born", "created_at", "is_active")
    list_filter = ("is_active",)
    search_fields = ("fullname", "bio")
    actions = ["activate", "deactivate"]
    ordering = ["id"]

    @admin.action(description="Mark selected author as active")
    def activate(self, request, queryset):
        queryset.update(is_active=True)

    @admin.action(description="Mark selected author as not active")
    def deactivate(self, request, queryset):
        queryset.update(is_active=False)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "name", )
    search_fields = ("name",)
    ordering = ["id"]

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "get_tags", "created_at")
    list_filter = ("tags",)
    search_fields = ("tags", "author", "quote")
    ordering = ["-id"]

    @admin.display(description='tags')
    def get_tags(self, obj):
        return [t.name for t in obj.tags.all()]
