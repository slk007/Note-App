from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=20)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    upadated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # to render detail page after a new NOTE is created
    def get_absolute_url(self):
        return reverse("notes_app:detail", kwargs={"pk": self.pk})
