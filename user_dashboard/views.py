from django.shortcuts import render
from blog.models import Work


# Create your views here.
def ProfileView(request):
    return render(request, 'user_dashboard/profile.html')