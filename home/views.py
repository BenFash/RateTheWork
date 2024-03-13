from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Q
from blog.models import Work

# Create your views here.
def Index(request):
    # Searchbar functionality
    query = request.GET.get('q')
    queryset = Work.objects.all().order_by("-created_on") 

    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(sub_category__icontains=query) |
            Q(categories__name__icontains=query) | 
            Q(user__username__icontains=query) 
        )

    context = {
        'query': query,
        'object_list': queryset,
    }
    return render(request, 'home/index.html', context)