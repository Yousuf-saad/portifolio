from django.db import models

# Create your models here.
class Technology(models.Model):
    name=models.CharField(max_length=50)
    icon=models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.name

class Project(models.Model):
    CATEGORY_CHOICES=[
        ("Web","Web Application"),
        ("Mobile","Mobile Application"),
        ("API","REST API"),
        ("AI","Artificial Intelligence"),
        ("Other","Other"),
    ]
    title=models.CharField(max_length=150,help_text="Project title.")
    slug=models.SlugField(unique=True,help_text="Unique URL slug.")
    short_description=models.TextField(help_text="Short description shown on project cards.")
    description=models.TextField(help_text="Detailed project description.")
    thumbnail=models.ImageField(upload_to='projects/',help_text="Project cover image.")
    category=models.CharField(max_length=20,choices=CATEGORY_CHOICES,default='web')
    github_url=models.URLField(blank=True,help_text="GitHub repository URL.")
    live_url=models.URLField(blank=True,help_text="Live demo URL.")
    featured=models.BooleanField(default=False,help_text="Show this project in the featured section.")
    display_order=models.PositiveIntegerField(default=0,help_text="Lower numbers appear first.")
    created_at=models.DateField(auto_now_add=True)
    technologies=models.ManyToManyField(Technology,blank=True,related_name="projects")
    class Meta:
        ordering=['display_order','-created_at']
    def __str__(self):
        return self.title

    