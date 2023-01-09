from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'index.html')

def aboutmcss(request):
    return render(request, 'aboutmcss.html')

def mcssadministration(request):
    return render(request, 'mcssadministration.html')

def news(request):
    return render(request, 'news.html')


def tubmanhigh(request):

    return render(request, 'schools/William-V.S.Tubman/tubmanhigh.html' )# This functions represents William V.S Tubman High

def tubman_admin(request):

    return render(request, 'schools/William-V.S.Tubman/tubman_admin.html' )

def Schedule(request):

    return render(request, 'schools/William-V.S.Tubman/Schedule.html' )