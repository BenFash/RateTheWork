from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Q
from .models import Work, Profile, Category

#Create your views here.
def work_list(request):
    queryset = Work.objects.filter(approved=True).order_by("-created_on")

    context = {
        'work': queryset,
        'paginate_by': 4,
    }
    return render(request, 'blog/posts.html', context)

