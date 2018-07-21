from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def default(request):
    return render(request,"default.html")

def zxqy(request):
    return render(request, "area.html")