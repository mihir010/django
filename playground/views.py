from django.shortcuts import render

# Create your views here.

# def calculate():
#     x = 3
#     y = 2
#     return x + y

def home(request):
    x = 1
    y = 2
    return render(request, "home.html")
