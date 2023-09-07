""" Models for user_app """
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from .constants import CNIC_VALIDATOR, CONTACT_NO_VALIDATOR


# models
class Profile(User):
    """Profile class inherited from django user class"""

    user_image = models.ImageField(upload_to="images/", default="images/empty.png")
    full_name = models.CharField(max_length=30, help_text="Enter your full name")
    gender_type = models.TextChoices("GenderType", "Male Female")
    user_gender = models.CharField(max_length=100, choices=gender_type.choices)
    user_DOB = models.DateField("date of birth", default=timezone.now)
    user_address = models.CharField(max_length=70, help_text="Enter Address")
    user_phone_no = models.CharField(
        max_length=100,
        validators=[CONTACT_NO_VALIDATOR],
        help_text="Enter your phone number 03xxxxxxxxx",
        unique=True,
    )
    user_cnic = models.CharField(
        max_length=15,
        validators=[CNIC_VALIDATOR],
        help_text="Enter cnic in format xxxxx-xxxxxxx-x",
        unique=True,
    )
    user_designation = models.CharField(
        max_length=40, help_text="Enter your designation", default=None
    )

    def __str__(self):
        return str(self.username)
