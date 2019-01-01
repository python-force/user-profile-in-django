from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.http import HttpResponseRedirect

from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Profile
from .forms import ProfileForm, CustomChangePasswordForm


def index(request):
    """Load Homepage"""
    profiles = Profile.objects.all().filter(user_id=request.user.id)
    return render(request, 'index.html', {'profiles': profiles})

def profiles(request):
    """Load Homepage"""
    profiles = Profile.objects.all().filter(user_id=request.user.id)
    return render(request, 'index.html', {'profiles': profiles})

@login_required
def profile(request, profile_slug):
    """Load Profile"""
    profile = get_object_or_404(Profile, slug=profile_slug)
    return render(request, 'profile.html', {'profile':profile})

@login_required
def edit_profile(request, profile_slug):
    profile = get_object_or_404(Profile, slug=profile_slug)
    form = ProfileForm(instance=profile)

    if request.method == "POST":
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "{} {}'s profile updated.".format(form.cleaned_data["first_name"], form.cleaned_data["last_name"]))
            return HttpResponseRedirect(profile.get_absolute_url())
    return render(request, "edit-profile.html", {'form':form})

@login_required
def change_password(request, profile_slug):
    if request.method == 'POST':
        form = CustomChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return HttpResponseRedirect('index')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = CustomChangePasswordForm(request.user)
    return render(request, 'change-password.html', {
        'form': form
    })

"""
def change_password(request, profile_slug):
    print(request.user)
    form = ChangePasswordForm(instance=request.user)

    if request.method == "POST":
        form = ChangePasswordForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "{} {}'s password updated.".format(form.cleaned_data["first_name"], form.cleaned_data["last_name"]))
            return HttpResponseRedirect(profile.get_absolute_url())
    return render(request, "change-password.html", {'form':form})
"""