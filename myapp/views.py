from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')  # This will look for an HTML file called 'home.html'