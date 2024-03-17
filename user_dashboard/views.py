from django.shortcuts import render, reverse
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ProfileForm
from blog.models import Rating


# Create your views here.
def ProfileView(request):
    """
    view for profile page
    """
    return render(request, 'user_dashboard/profile.html')



def UploadProfilePic(request):
    """
    view for upload profile picture page
    """
    if request.method == 'POST':
        profile_pic_form = ProfileForm(request.POST, request.FILES)
        if profile_pic_form.is_valid():
            pic_form = profile_pic_form.save(commit=False)
            pic_form.user = request.user            
            pic_form.save()
            messages.success(request, 'Profile picture uploaded successfully.')
            return HttpResponseRedirect(reverse('profile'))
    else:
        profile_pic_form = ProfileForm()

    return render(request, 'user_dashboard/profile_picture.html', {
        'profile_pic_form': profile_pic_form,
    })


def ProfileComments(request):
    """
    View for the profile comments page
    """
    user_ratings = Rating.objects.filter(user=request.user).order_by("-created_on")

    context = {
        'user_ratings': user_ratings,
    }

    return render(request, 'user_dashboard/profile_comments.html', context)
