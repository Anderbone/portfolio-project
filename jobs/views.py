from django.shortcuts import render
import sys
sys.path.append('../')
from .models import Job
# from ..blog.models import Blog
from blog.models import Blog

# Create your views here.

# def home(request):
#     jobs = Job.objects
#     return render(request, 'jobs/home.html', {'jobs':jobs})

# def webcv(request):
#     return render(request, 'jobs/cv.html')

def home(request):
    blogs = Blog.objects
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'blogs':blogs})