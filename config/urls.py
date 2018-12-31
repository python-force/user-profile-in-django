"""minerals URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings

from profiles.core import views as core_views
from profiles.accounts import views as accounts_views

urlpatterns = [
    path(r'markdownx/', include('markdownx.urls')),
    path('accounts/', include('profiles.accounts.urls', namespace='accounts')),
    path('profiles/<slug:profile_slug>/change-password', core_views.change_password, name="change-password"),
    path('profiles/<slug:profile_slug>/edit', core_views.edit_profile, name="edit-profile"),
    path('profiles/<slug:profile_slug>/', core_views.profile, name="profile"),
    path('', core_views.index, name="index"),
    path('admin/', admin.site.urls),
]