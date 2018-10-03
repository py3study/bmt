from django.shortcuts import render,HttpResponse

def index(request):
    return render(request,"index.html")

def default(request):
    return render(request,"default.html")

def user_list(request):
    return render(request,"user_list.html")

