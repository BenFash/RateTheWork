from django.shortcuts import render

# Create your views here.
def About(request):
    """
    view for about page
    """
    return render(request, 'about/about.html')