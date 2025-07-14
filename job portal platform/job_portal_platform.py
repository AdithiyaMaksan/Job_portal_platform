## Job Portal Platform - Django Project Structure with DRF APIs

# 1. Create Project and App
# Run these commands:
# django-admin startproject jobportal
# cd jobportal
# python manage.py startapp core

# 2. Project Structure:
# jobportal/
# ├── core/
# │   ├── admin.py
# │   ├── apps.py
# │   ├── models.py
# │   ├── serializers.py
# │   ├── views.py
# │   ├── urls.py
# │   └── templates/
# │       └── core/
# │           ├── home.html
# │           ├── job_list.html
# │           ├── job_detail.html
# │           ├── login.html
# │           └── register.html
# ├── jobportal/
# │   ├── settings.py
# │   ├── urls.py
# │   └── wsgi.py
# ├── db.sqlite3
# └── manage.py

# 3. Models (core/models.py)
from django.contrib.auth.models import User
from django.db import models

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField()
    applied_at = models.DateTimeField(auto_now_add=True)

# 4. Admin Registration (core/admin.py)
from django.contrib import admin
from .models import Company, Job, Application

admin.site.register(Company)
admin.site.register(Job)
admin.site.register(Application)

# 5. Serializers (core/serializers.py)
from rest_framework import serializers
from .models import Job, Company, Application

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'

# 6. Views (core/views.py)
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Job, Application
from rest_framework import viewsets
from .serializers import JobSerializer, CompanySerializer, ApplicationSerializer


def home(request):
    jobs = Job.objects.all()
    return render(request, 'core/home.html', {'jobs': jobs})

def job_detail(request, job_id):
    job = Job.objects.get(id=job_id)
    return render(request, 'core/job_detail.html', {'job': job})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'core/register.html', {'form': form})

# API Views
class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

# 7. URLs (core/urls.py)
from django.urls import path, include
from . import views
from rest_framework import routers
from .views import JobViewSet, CompanyViewSet, ApplicationViewSet

router = routers.DefaultRouter()
router.register(r'jobs', JobViewSet)
router.register(r'companies', CompanyViewSet)
router.register(r'applications', ApplicationViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),
    path('register/', views.register, name='register'),
    path('api/', include(router.urls)),
]

# 8. Main URLs (jobportal/urls.py)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('api-auth/', include('rest_framework.urls')),
]

# 9. Templates (basic example)
# home.html
# {% for job in jobs %}
#   <a href="{% url 'job_detail' job.id %}">{{ job.title }}</a><br>
# {% endfor %}

# 10. Settings (Add 'core' and 'rest_framework' to INSTALLED_APPS)
# settings.py
# INSTALLED_APPS = [..., 'core', 'rest_framework']
# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR / 'media'

# 11. Run
# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver
