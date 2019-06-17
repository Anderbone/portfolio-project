from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField(null=True, blank=True)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')