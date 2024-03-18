from django.shortcuts import render, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import UserContactAdminForm
from .models import UserContactAdmin

def ContactAdmin(request):
    """
    Contact admin view
    """
    contactadmin = UserContactAdmin.objects.all().order_by('-created_at').first()
    
    if request.method == 'POST':
        user_contact_admin_form = UserContactAdminForm(request.POST, request.FILES)
        if user_contact_admin_form.is_valid():         
            user_contact_admin_form.save()
            messages.success(request, 'Message sent successfully. Please expect a response within 3 working days.')
            return HttpResponseRedirect(reverse('home'))
    else:
        user_contact_admin_form = UserContactAdminForm()

    return render(request, 'contact/contact.html', {
        'contactadmin' : contactadmin,
        'user_contact_admin_form': user_contact_admin_form,
    })

