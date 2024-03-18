from django.shortcuts import render, reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ProfileForm, ContactAdminForm
from blog.models import Work, Rating
from .models import ContactAdmin


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



def ProfilePosts(request):
    """
    View for the profile posts page
    """
    user_posts = Work.objects.filter(user=request.user).order_by("-created_on")

    items_per_page = 4

    paginator = Paginator(user_posts, items_per_page)
    page_number = request.GET.get('page')
    try:
        user_posts = paginator.page(page_number)
    except PageNotAnInteger:
        user_posts = paginator.page(1)
    except EmptyPage:
        user_posts = paginator.page(paginator.num_pages)

    context = {
        'user_posts': user_posts,
    }

    return render(request, 'user_dashboard/profile_posts.html', context)



def ProfileLikes(request):
    """
    View for the profile likes page
    """
    user_likes = Work.objects.filter(likes=request.user).order_by("-created_on")

    items_per_page = 4

    paginator = Paginator(user_likes, items_per_page)
    page_number = request.GET.get('page')
    try:
        user_likes = paginator.page(page_number)
    except PageNotAnInteger:
        user_likes = paginator.page(1)
    except EmptyPage:
        user_likes = paginator.page(paginator.num_pages)


    context = {
        'user_likes': user_likes,
    }

    return render(request, 'user_dashboard/profile_likes.html', context)



def ProfileContact(request):
    """
    View for the contact admin page
    """
    contactadmin = ContactAdmin.objects.all().order_by('-created_at').first()
    contact_admin_form = ContactAdminForm() 
    
    if request.method == 'POST':
        contact_admin_form = ContactAdminForm(request.POST, request.FILES)
        if contact_admin_form.is_valid():
            contact_ad_form = contact_admin_form.save(commit=False)
            contact_ad_form.user = request.user            
            contact_ad_form.save()
            messages.success(request, 'Message sent successfully. Please expect a response within 3 working days.')
            return HttpResponseRedirect(reverse('profile'))

    return render(request, 'user_dashboard/profile_contact.html', {
        'contactadmin' : contactadmin,
        'contact_admin_form': contact_admin_form,
    })