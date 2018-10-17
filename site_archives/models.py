from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS_CHOICES = (
    ('u', 'Undone'),
    ('p', 'In Progress'),
    ('d', 'Done'),
)


class Archive(models.Model):
    old_url = models.URLField(max_length=400)
    new_url = models.URLField(max_length=400, null=True, blank=True)
    status = models.CharField(max_length=1,
                              choices=STATUS_CHOICES, default="n")
    archive_online = models.BooleanField(default=False)
    screenshot = models.ImageField(null=True, blank=True)
    short_desc = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User,models.SET_NULL,null=True)
