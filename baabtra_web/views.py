from django.shortcuts import render

# Create your views here.
def b_h(request):
    return render(request,'baabtraweb/home.html')
def index(request):
    return render(request,'baabtraweb/index.html')