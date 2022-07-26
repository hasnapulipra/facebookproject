from django.shortcuts import render

# Create your views here.

def fbpage(request):
    return render(request,'fbpage.html')