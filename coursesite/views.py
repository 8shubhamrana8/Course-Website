from django.shortcuts import render
from courses.models import Courses

def home(request):
    courses = Courses.objects.all()
    return render(request, 'website/index.html', {'courses':courses})