from django.shortcuts import render,get_object_or_404
from .models import Project
# Create your views here.
def project_detail(request,slug):
    project=get_object_or_404(Project.objects.prefetch_related("technologies"),slug=slug)
    context={
        "project":project
    }
    return render(request,"projects/detail.html",context)