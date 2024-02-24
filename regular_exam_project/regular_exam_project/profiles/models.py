from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, MinValueValidator, EmailValidator, MinLengthValidator
from django.db import models


def validate_age(value):
    if value < 21:
        raise ValidationError("Age requirement: 21 years and above.")

class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        unique=True,
        validators=[
            MinLengthValidator(3, message="Username must be at least 3 chars long!"),
            RegexValidator(r'^\w+$', message="Username must contain only letters, digits, and underscores!"),
        ]
    )
    email = models.EmailField(
        unique=True,
        validators=[EmailValidator()]
    )
    age = models.IntegerField(
        validators=[validate_age]
    )
    password = models.CharField(
        max_length=20
    )
    first_name = models.CharField(
        max_length=25,
        blank=True
    )
    last_name = models.CharField(
        max_length=25,
        blank=True
    )
    profile_picture = models.URLField(
        blank=True
    )

    def __str__(self):
        return self.username
