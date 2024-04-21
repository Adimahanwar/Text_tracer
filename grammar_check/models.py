from django.db import models

class Sentence(models.Model):
    text = models.TextField()
    improved_text = models.TextField(blank=True, null=True)
