from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def Index(request):
    return render(request, 'home/index.html')