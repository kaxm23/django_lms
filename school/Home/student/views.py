
# Create your views here.
from django.shortcuts import render

def students(request):
    return render(request, "students.html")
