from django.contrib import admin
from .models import Profile,About,Skill,Education,Experience,ContactMessage

# Register your models here.
@admin.register(Profile)
class profileAdmin(admin.ModelAdmin):
    list_display=('full_name','profession','email')
    search_fields=('full_name','profession')

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display=(
        "title",
        "years_experience",
        "total_projects",
    )
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display=(
        'name',
        'category',
        'percentage',
    )
    list_filter=('category',)
    search_fields=('name',)

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = (
        "degree",
        "institution",
        "start_year",
        "end_year",
    )
    list_filter = (
        "start_year",
        "end_year",
    )
    search_fields = (
        "degree",
        "institution",
    )
    ordering = (
        "display_order",
        "-end_year",
    )

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):

    list_display = (
        "job_title",
        "company",
        "start_date",
        "end_date",
        "current",
    )
    list_filter = (
        "current",
        "company",
    )
    search_fields = (
        "job_title",
        "company",
        "description",
    )
    ordering = (
        "display_order",
        "-start_date",
    )

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "subject",
        "created_at",
        "is_read",
    )

    list_filter = (
        "is_read",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "subject",
        "message",
    )

    readonly_fields = ("created_at",)

    list_editable = ("is_read",)
