from django.db import models
from django.contrib.auth.models import User


CATEGORY_CHOICES = (
    ('personal', 'Personal'),
    ('group', 'Group'),
)

# Type choices for gigs
TYPE_CHOICES = (
    ('front_end', 'Front End'),
    ('back_end', 'Back End'),
    ('mobile', 'Mobile'),
    ('design', 'Design'),
)
# Create your models here.
class Gigs(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    gigName = models.CharField(null=True, blank=True, max_length=200)
    gigCategory = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    gigDuration = models.DurationField()
    clientName = models.CharField(null=True, blank=True, max_length=200)
    gigAmount = models.CharField()
    paymentType = models.CharField()
    startingAmount = models.CharField()
    gigType = models.CharField(max_length=20, choices=TYPE_CHOICES)

    def __str__(self):
        return self.gigName