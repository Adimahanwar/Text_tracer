from django.db import models

class HandwrittenText(models.Model):
    image = models.ImageField(upload_to='handwritten_images/')
    text = models.TextField(blank=True, null=True)
