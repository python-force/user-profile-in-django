from django.urls import reverse
from django.test import TestCase
from django.utils import timezone

from django.contrib.auth.models import User
from profiles.core.models import Profile
from django.test import Client


class ProfileModelTests(TestCase):
    """Test for Profile Model"""
    def test_profile_creation(self):
        """Test to create profile"""
        profile = Profile.objects.create(
            user=User.objects.create(username='john',
                                    email='jlennon@beatles.com',
                                    password='doe'),
            first_name="Radek",
            last_name="Doe",
            email="s@d.com",
            email_verify="s@d.com",
            date_of_birth="2018-12-28",
        )
        now = timezone.now()
        self.assertLess(profile.pub_date, now)



"""
class ProfileViewsTests(TestCase):
    def setUp(self):
        self.profile = Profile.objects.create(
            user=User.objects.create(username='Lea',
                                 email='lea@beatles.com',
                                 password='doelea'),
            first_name="Lea",
            last_name="Doe",
            email="ss@dd.com",
            email_verify="ss@dd.com",
            date_of_birth="2018-12-29",
        )
        now = timezone.now()
        self.assertLess(self.profile.pub_date, now)

    def test_index(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.profile, resp.context['profiles'])
        self.assertTemplateUsed(resp, 'index.html')

    def test_course_detail_view(self):
        resp = self.client.get(reverse('detail',
                                       kwargs={'pk': self.mineral.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral, resp.context['mineral'])
        self.assertTemplateUsed(resp, 'detail.html')
    """