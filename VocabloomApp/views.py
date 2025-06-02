from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index2.html')

def courses(request):
    return render(request, 'courses.html')

def course(request):
    return render(request, 'course.html')

def blog(request):
    return render(request, 'blog.html')

def blog_single(request):
    return render(request, 'blog_single.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def login(request):
    return render(request, 'login.html')

def adminHome(request):
    return render(request,'Admin/index.html')