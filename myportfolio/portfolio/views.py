from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.forms import modelformset_factory
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from collections import Counter

from .models import Project, Tag
from .forms import *
#########################################
# Default Pages
#########################################
def home(request):
    current_user = request.user
    recent_projects = Project.objects.order_by("-date_posted")[:6]
    intro_content = IntroContent.objects.first()

    context = {
        'intro_content':intro_content,
        'projects':recent_projects
    }

    template_name = 'main.html'
    return render(request, template_name, context)

def portfolio(request):
    projects = Project.objects.all()
    recent = projects[:3]
    tags = Tag.objects.all()

    tag_dict = {}
    for tag in tags:
        proj_count = tag.project_set.count()
        tag_dict[proj_count] = tag
    print(tag_dict)
    greatest = 0
    least = 0
    popular_tags = []
    for key, value in tag_dict.items():
        if len(popular_tags) <= 3:
            if key > greatest:
                greatest = key
                popular_tags.append(value)
            elif key >= least and key <= greatest and key != 0:
                popular_tags.append(value)
                least = key
        
        print(key)
        print(value)
    
    context = {
        'recent': recent,
        'popular_tags':popular_tags,
        'projects':projects,
    }
    
    template_name = 'portfolio.html'

    return render(request, template_name, context)

def project(request, pname):
    project = Project.objects.get(name=pname)
    images = project.image_set.all()
    context = {
        'project':project,
        'images':images,
        'cols':[[0,1,2,3],[4,5,6,7],[8,9,10,11]],
    }
    
    template_name = 'project.html'

    return render(request, template_name, context)

def resume(request):
    context = {}
    template_name = 'resume.html'

    return render(request, template_name, context)

#########################################
# Project CRUD
#########################################

def newProject(request):
    form = ProjectForm()
    # form = ProjectForm(request.POST or None)
    # print(form)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data['tags',])
            project = form.save()

            # name = request.POST.get("name")
            # desc = request.POST.get("desc")
            # desc_short = request.POST.get("desc_short")
            # desc_design = request.POST.get("desc_design")

            # client = request.POST.get("client")
            # date = request.POST.get("date")
            # basedin = request.POST.get("basedin")
            # website = request.POST.get("website")
            # github = request.POST.get("name")

        

            # project = Project(id=IDgenerator(), name=name, desc=desc, desc_short=desc_short, desc_design=desc_design, client=client, date=date, basedin=basedin, website=website, github=github, tags=tags)

            # project.save()
            images = request.FILES.getlist("file[]")
            # print(images)
            
            for img in images:
                fs = FileSystemStorage()
                file_path = fs.save(img.name, img)

                image = Image(project=project, image=file_path)
                image.save()
            
            
            return redirect(portfolio)

    template_name = "createpost.html"
    context = {'form':form}
    return render(request, template_name, context)

# def newProjectSave(request):
#     name = request.POST.get("name")
#     desc = request.POST.get("desc")
#     desc_short = request.POST.get("desc_short")
#     desc_design = request.POST.get("desc_design")

#     client = request.POST.get("client")
#     date = request.POST.get("date")
#     basedin = request.POST.get("basedin")
#     website = request.POST.get("website")
#     github = request.POST.get("name")

#     images = request.FILES.getlist("file[]")
#     print(images)

#     project = Project(id=IDgenerator(), name=name, desc=desc, desc_short=desc_short, desc_design=desc_design, client=client, date=date, basedin=basedin, website=website, github=github)

#     project.save()

#     for img in images:
#         fs = FileSystemStorage()
#         file_path = fs.save(img.name, img)

#         image = Image(project=project, image=file_path)
#         image.save()
    
#     return redirect(portfolio)
    # return HttpResponse("Files Uploaded")

import random
def IDgenerator():
    number = random.randint(1,10000)

    while Project.objects.filter(id=number).exists():
        number += 1

    return number


def updateProject(request, pname):
    project = Project.objects.get(name=pname)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('/portfolio/')
    
    context = {'form':form}
    template_name = 'createpost.html'

    return render(request, template_name, context)

#########################################
# Sign In and Logout
#########################################
def signIn(request):
    if request.user.is_authenticated:
        messages.add_message(request, messages.INFO, 'You are already signed in.') 
        # messages.info(request, "You are already signed in.")
        # # return redirect(home)
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            login(request, user)
            
            print("logged in")
            context = {'messages' : None}
            return redirect(home)
    
    context = {}
    template_name = 'signin.html'
    
    return render(request, template_name, context)

def logOut(request):
    messages.success(request, 'Logged out')
    logout(request)
    print(request.user)
    return redirect('home')