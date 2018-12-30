from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Profile
from .forms import ProfileForm


def index(request):
    """Load Homepage"""
    profiles = get_list_or_404(Profile)
    return render(request, 'index.html', {'profiles': profiles})

def profile(request, profile_slug):
    """Load Profile"""
    profile = get_object_or_404(Profile, slug=profile_slug)
    return render(request, 'profile.html', {'profile':profile})


def edit_profile(request, profile_slug):
    profile = get_object_or_404(Profile, slug=profile_slug)
    form = ProfileForm(instance=profile)
    return render(request, "edit-profile.html", {'form':form})