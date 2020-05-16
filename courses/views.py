from django.shortcuts import render

# Create your views here.
from .models import Course
def allcourses(request):
    course=Course.objects
    return render(request,'courses/home.html',{'course':course})