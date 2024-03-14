from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from .models import Work, Rating
from .forms import RatingForm

#Create your views here.
def WorkList(request):
    """
    view for the work page
    """
    queryset = Work.objects.filter(approved=True).order_by("-created_on")

    context = {
        'work': queryset,
        'paginate_by': 4,
    }
    return render(request, 'blog/posts.html', context)


def WorkDetail(request, pk):
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


class WorkDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    view for the work delete page
    """
    model = Work
    template_name = 'blog/work_delete.html'
    success_url = '/work/'

    def test_func(self):
        return self.request.user == self.get_object().user


# class WorkEdit(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     """
#     view for the work edit page
#     """
#     model = Work
#     template_name = 'blog/work_edit.html'
#     form_class 
#     success_url = '/work/'

#     def test_func(self):
#         return self.request.user == self.get_object().user



class CommentDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    view for the comment delete page
    """
    model = Rating
    template_name = 'blog/comment_delete.html'
    success_url = '/work/'

    def test_func(self):
        return self.request.user == self.get_object().user

class CommentEdit(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    view for the comment edit page
    """
    model = Rating
    template_name = 'blog/comment_edit.html'
    form_class = RatingForm
    success_url = '/work/'

    def test_func(self):
        return self.request.user == self.get_object().user


def WorkLike(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('work_detail', args=[pk]))

