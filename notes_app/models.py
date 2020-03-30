from django.db import models
from django.urls import reverse

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    upadated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("notes_app:detail", kwargs={"pk": self.pk})
    