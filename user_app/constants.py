""" Constants declared to be used in user app """
from django.core.validators import RegexValidator

CNIC_VALIDATOR = RegexValidator(
    "\d{5}\-\d{7}\-\d{1}", "CNIC format needs to be xxxxx-xxxxxxx-x"
)
CONTACT_NO_VALIDATOR = RegexValidator(
    "03\d{9}$", "Phone number format needs to be 03xxxxxxxxx"
)

GENDER_CHOICES = (("M", "Male"), ("F", "Female"), ("", "Do not specify"))
