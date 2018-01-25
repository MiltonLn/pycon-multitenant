from django.db import models


class Note(models.Model):
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
