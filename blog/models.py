from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField(null=True, blank=True)
    body = models.TextField()
    test2 = models.CharField()
    summary = models.TextField()
    # image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.summary

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')