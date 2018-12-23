from django.shortcuts import render, get_object_or_404
# from .models import Mineral


def index(request):
    """Load Homepage"""
    return render(request, 'index.html', {})