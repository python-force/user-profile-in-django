from django.urls import reverse
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# import pytz
from django.utils.text import slugify

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    date_of_birth = models.DateField(max_length=12, blank=True)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(blank=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify("{}-{}-{}".format(self.first_name.lower(), self.last_name.lower(), self.id))
        super().save(*args, **kwargs)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('profile', args=[str(self.slug)])