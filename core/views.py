from django.shortcuts import render #    get_object_or_404, redirect, 
from django.contrib.auth.decorators import login_required
from core.forms import EditProfileForm
from django.contrib import messages
# from django.urls import is_valid_path
# from django.contrib.auth.forms import UserChangeForm

# Create your views here.

@login_required
def edit_user_details(request):
    """A page for the user to view and update their details."""
    # user = get_object_or_404(user, id=request.user)

    page_title = 'Name'

    if request.method != 'POST':
        form = EditProfileForm(instance=request.user)
        message = ''
    else:
        form = EditProfileForm(instance=request.user, data=request.POST)

        if form.is_valid():
            form.save()
            message = 'Details saved'

    messages.success(request, message )

    context = {'user': request.user, 'message': message, 'form': form, 'page_title': page_title }

    return render(request, "edit_user_details.html", context )