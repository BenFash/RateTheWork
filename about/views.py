from django.shortcuts import render


def About(request):
    """
    view for about page
    """
    return render(request, 'about/about.html')
