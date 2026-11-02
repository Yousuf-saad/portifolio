from django.contrib import admin
from .models import Project,Technology
# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display=(
        "title",
        "category",
        "featured",
        "display_order",
    )
    list_filter=(
        "category",
        "featured",
    )
    search_fields=(
        "title",
        "technologies",
    )
    prepopulated_fields={
        "slug":("title",)
    }
    filter_horizontal=("technologies",)

@admin.register(Technology)
class TechnologiesAdmin(admin.ModelAdmin):
    list_display=(
        "name",
        "icon"
    )
    search_fields=("name",)