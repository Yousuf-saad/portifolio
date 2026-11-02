from django.shortcuts import render,redirect
from portfolio.models import Profile,About,Skill,Education,Experience
from projects.models import Project
from portfolio.forms import ContactForm
from django.contrib import messages
# Create your views here.
def home(request):
    context={
        'profile':Profile.objects.first(),
        'about':About.objects.first(),
        'skills':Skill.objects.all(),
        'education':Education.objects.all(),
        'experience':Experience.objects.all(),
        'projects':Project.objects.prefetch_related("technologies").all(),
    }
    return render(request,'home/index.html',context)

def contact_submit(request):
    if request.method!="POST":
        return redirect("/#contact")
    form=ContactForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request,"Your message has been sent successfully!")
    else:
        messages.error(
            request,
            "Please correct the form errors and try again."
        )
    return redirect("/#contact")