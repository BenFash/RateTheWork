from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
    paginator = Paginator(queryset, 4)
    page_number = request.GET.get('page')
    try:
        work = paginator.page(page_number)
    except PageNotAnInteger:
        work = paginator.page(1)
    except EmptyPage:
        work = paginator.page(paginator.num_pages)

    context = {
        'query': query,
        'work': work,
    }
    return render(request, 'home/index.html', context)
