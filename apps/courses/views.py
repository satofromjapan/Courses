from django.shortcuts import render, redirect
from .models import Course
# Create your views here.
def index(request):
    courses = Course.objects.all()
    context = {"courses": courses}
    return render(request, 'courses/index.html', context)

def create(request):
    Course.objects.create(name=request.POST['name'], description=request.POST['description'])
    return redirect('/')

def remove(request,id):
    course = Course.objects.filter(id=id)
    context = {"course": course}
    return render(request, 'courses/delete.html', context)

def remove_confirm(request, id):
    course = Course.objects.get(id=id)
    Course.objects.filter(id=id).delete()
    return redirect('/')
