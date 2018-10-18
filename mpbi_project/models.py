from django.db import models
from django.utils.timezone import now as timezone_now


class Contact(models.Model):
    name = models.CharField(max_length=255, blank=True, default='')
    email = models.EmailField(max_length=255, blank=True, default='')
    message = models.TextField(max_length=2000, blank=True, default='')
    date = models.DateTimeField(blank=True, default=timezone_now)

    class Meta:
        ordering = [
            "email", "date"]
        verbose_name = u'Contact Submission'
        verbose_name_plural = u'Contact Submissions'



