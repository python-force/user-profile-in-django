from django.shortcuts import render, get_object_or_404
from .models import Profile


def index(request):
    """Load Homepage"""
    return render(request, 'index.html', {})

def profile(request, slug):
    """Load Profile"""
    profile = get_object_or_404(Profile, slug=slug)
    return render(request, 'profile.html', {'profile':profile})