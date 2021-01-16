"""myportfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from portfolio.views import *

urlpatterns = [
    # Default Pages
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('portfolio/', portfolio, name='portfolio'),
    path('project/<str:pname>', project, name='project'),
    path('resume/', resume, name='resume'),

    # # Project CRUD
    path('newproject/', newProject, name='new_project'),
    # path('newproject_save/', newProjectSave, name='new_project_save'),
    path('updateproject/<str:pname>/', updateProject, name='update_project'),

    # Sign in
    path('signin/', signIn, name='sign_in'),
    path('logout/', logOut, name='log_out'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
