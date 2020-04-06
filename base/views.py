from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'base/home.html')

def resume(resquest):
    return render(request, 'base/resume.html')