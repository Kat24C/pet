from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField


class Profile(models.Model):
    """
    A user profile model for maintaining information.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=40, null=True, blank=True)
    surname = models.CharField(max_length=40, null=True, blank=True)
    phone_number = PhoneNumberField(blank=True, unique=True)
    street_address1 = models.CharField(max_length=150, null=True, blank=True)
    street_address2 = models.CharField(max_length=150, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=True, blank=True)
    county = models.CharField(max_length=50, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(blank_label='IE', default='IE',
                           blank=True)

    def __str__(self):
        return self.user.username
