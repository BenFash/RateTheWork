from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def work_list(request):
    queryset = Work.objects.filter(status=1).order_by("-created_on")
    context = {
        'object_list': queryset,
        'paginate_by': 4,
    }
    return render(request, 'posts.html', context)