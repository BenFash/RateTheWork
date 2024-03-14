from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Q
from .models import Work, Rating
from .forms import RatingForm

#Create your views here.
def work_list(request):
    """
    view for the post page
    """
    queryset = Work.objects.filter(approved=True).order_by("-created_on")

    context = {
        'work': queryset,
        'paginate_by': 4,
    }
    return render(request, 'blog/posts.html', context)


def work_detail(request, pk):
    """
    view for the work detail page
    """
    queryset = Work.objects.filter(approved=True)
    work = get_object_or_404(queryset, pk=pk)
    ratings = Rating.objects.filter(approved=True).order_by("-created_on")
    liked = False
    if request.user.is_authenticated and work.likes.filter(id=request.user.id).exists():
        liked = True

    if request.method == 'POST':
        rating_form = RatingForm(data=request.POST)
        if rating_form.is_valid():
            rating = rating_form.save(commit=False)
            rating.work = work
            rating.user = request.user
            rating.save()
            rating_form = RatingForm()
            return render(request, "blog/work_details.html", {
                "work": work,
                "ratings": ratings,
                "commented": True,
                "rating_form":  rating_form,
                "liked": liked
            })
    else:
        rating_form = RatingForm()

    return render(request, "blog/work_details.html", {
        "work": work,
        "ratings": ratings,
        "commented": False,
        "rating_form": rating_form,
        "liked": liked
    })



def work_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('work_detail', args=[slug]))


def comment_edit(request, slug, rating_id):
    """
    View to edit comments
    """
    if request.method == "POST":
        queryset = Work.objects.filter(approved=True)
        work = get_object_or_404(queryset, pk=pk)

        rating = get_object_or_404(Rating, pk=rating_id)
        rating_form = RatingForm(data=request.POST, instance=rating)

        if rating_form.is_valid() and rating.user == request.user:
            rating = rating_form.save(commit=False)
            rating.work = work
            rating.approved = False
            rating.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('work_detail', args=[pk]))