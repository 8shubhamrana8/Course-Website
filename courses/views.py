from django.shortcuts import render, get_object_or_404
from .models import Courses

# Create your views here.
def courses(request):
    courses = Courses.objects.all()
    return render(request, 'courses.html', {'courses':courses})

def course_details(request, course_id):
    course = get_object_or_404(Courses, id=course_id)
    return render(request, 'course_details.html', {'course': course})