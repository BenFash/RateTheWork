from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.db.models import Q
from blog.models import Work

def Index(request):
    # Searchbar functionality
    query = request.GET.get('q')
    queryset = Work.objects.filter(approved=True).order_by("-created_on")

    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(sub_category__icontains=query) |
            Q(categories__name__icontains=query) | 
            Q(user__username__icontains=query) 
        )


    # Pagination
    items_per_page = 4
    paginator = Paginator(queryset, items_per_page)
    page_number = request.GET.get('page')
    try:
        object_list = paginator.page(page_number)
    except PageNotAnInteger:
        object_list = paginator.page(1)
    except EmptyPage:
        object_list = paginator.page(paginator.num_pages)

    context = {
        'query': query,
        'object_list': object_list,
    }
    return render(request, 'home/index.html', context)