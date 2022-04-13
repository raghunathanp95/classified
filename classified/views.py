from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    return render(request,"index.html")

def aboutUS(request):
    return HttpResponse("Welcome to Django")

def Course(request):
    return HttpResponse("Welcome to this Course")

def CourseDetails(request,courseID):
    return HttpResponse(courseID)