from django.urls import reverse
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from image_cropping import ImageRatioField

# import pytz
from django.utils.text import slugify

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    email_verify = models.EmailField(max_length=100)
    date_of_birth = models.DateField(max_length=12)
    bio = models.TextField()
    avatar = models.ImageField(blank=True)
    avatar_cropping = ImageRatioField('avatar', '430x360')
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    country_of_residence = models.CharField(max_length=255, blank=True)
    favorite_animal = models.CharField(max_length=255, blank=True)
    hobby = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify("{}-{}-{}".format(self.first_name.lower(), self.last_name.lower(), self.id))
        super().save(*args, **kwargs)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('profile', args=[str(self.slug)])

    def display_bio(self):
        return mark_safe(self.bio)