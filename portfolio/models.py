from django.db import models

# Create your models here.
class Profile(models.Model):
    full_name=models.CharField(max_length=100)
    profession=models.CharField(max_length=100)
    about=models.TextField()
    profile_image=models.ImageField(upload_to="profile/")
    resume=models.FileField(upload_to="resume/")
    github=models.URLField(blank=True)
    linkedin=models.URLField(blank=True)
    instagram=models.URLField(blank=True)
    whatsapp=models.URLField(blank=True)
    email=models.EmailField()
    phone=models.CharField(max_length=20)
    location=models.CharField(max_length=100)
    def __str__(self):
        return self.full_name

class About(models.Model):
    title=models.CharField(max_length=100,default="About Me")
    description=models.TextField()
    years_experience=models.PositiveIntegerField(default=0)
    total_projects=models.PositiveIntegerField(default=0)
    technologies=models.PositiveIntegerField(default=0)
    certifications=models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title

class Skill(models.Model):
    CATEGORY_CHOICES=[
        ("Backend","Backend"),
        ("Frontend","Frontend"),
        ("Database","Database"),
        ("Tools","Tools"),
    ]
    name=models.CharField(max_length=50,help_text="Enter the skill name (e.g. Python,Django,React).")
    category=models.CharField(max_length=50,choices=CATEGORY_CHOICES,help_text="Select the category this skill belongs to.")
    percentage=models.PositiveIntegerField(default=80,help_text="Enter your proficiency level (0-100).")
    icon=models.CharField(max_length=100,blank=True,help_text="Enter the Font Awesome class (e.g 'fa-brands fa-python' or 'fa-solid fa-database').")
    class Meta:
        ordering=['category','name']
        verbose_name='Skill'
        verbose_name_plural="Skills"

    def __str__(self):
        return self.name

class Education(models.Model):
    degree=models.CharField(max_length=150,help_text="Degree or qualification name")
    institution=models.CharField(max_length=200,help_text="College,university, or institution name")
    start_year=models.PositiveIntegerField(help_text="Starting year, e.g. 2022.")
    end_year=models.PositiveIntegerField(help_text="Ending year, e.g. 2025. Leave blank if currently pursuing.")
    description=models.TextField(blank=True,help_text="Short description about your education.")
    display_order=models.PositiveIntegerField(default=0,help_text="Lower appears first")
    class Meta:
        ordering=["display_order","-end_year"]
    def __str__(self):
        return f"{self.degree}-{self.institution}"

class Experience(models.Model):
    job_title=models.CharField(max_length=150,help_text="Your job title or role")
    company=models.CharField(max_length=200,help_text="Company or Organisation")
    location=models.CharField(max_length=150,blank=True,help_text="Job location, e.g. Kerala,India")
    start_date = models.DateField(
        help_text="Employment start date."
    )
    end_date = models.DateField(
        null=True,
        blank=True,
        help_text="Leave blank if this is your current position."
    )
    current = models.BooleanField(
        default=False,
        help_text="Enable this if this is your current position."
    )
    description=models.TextField(help_text="Describe your responsibilties and achievements.")
    display_order = models.PositiveIntegerField(
        default=0,
        help_text="Lower numbers appear first."
    )
    class Meta:
        ordering = ["display_order", "-start_date"]
    def __str__(self):
        return f"{self.job_title} - {self.company}"


class ContactMessage(models.Model):

    name = models.CharField(
        max_length=100,
        help_text="Visitor's full name."
    )

    email = models.EmailField(
        help_text="Visitor's valid email address."
    )

    subject = models.CharField(
        max_length=150,
        help_text="Subject of the message."
    )

    message = models.TextField(
        help_text="Message sent by the visitor."
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    is_read = models.BooleanField(
        default=False,
        help_text="Mark this message as read after reviewing it."
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"

    def __str__(self):
        return f"{self.name} - {self.subject}"
