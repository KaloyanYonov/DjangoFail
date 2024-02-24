from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from regular_exam_project.profiles.models import Profile

CAR_TYPES = [
    ('Rally', 'Rally'),
    ('Open-wheel', 'Open-wheel'),
    ('Kart', 'Kart'),
    ('Drag', 'Drag'),
    ('Other', 'Other'),
]

def validate_year(value):
    if not (1999 <= value <= 2030):
        raise ValidationError("Year must be between 1999 and 2030!")

class Car(models.Model):
    type = models.CharField(
        max_length=10,
        choices=CAR_TYPES
    )
    model = models.CharField(
        max_length=15
    )
    year = models.IntegerField(
        validators=[validate_year]
    )
    image_url = models.URLField(
        unique=True,
        default="https://...",
        error_messages={'unique': "This image URL is already in use! Provide a new one."}
    )
    price = models.FloatField(
        validators=[MinValueValidator(1.0)]
    )
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='cars', blank=True)

    def __str__(self):
        return f"{self.model} ({self.year})"
