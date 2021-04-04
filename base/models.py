from django.db import models
import uuid


SITE_URL = 'http://127.0.0.1:8000/'


class Link(models.Model):
    url = models.URLField(max_length=400)
    code = models.CharField(max_length=6, unique=True, default=uuid.uuid4().hex[:6].upper())

    @property
    def short_url(self):
        return SITE_URL + self.url

    def __str__(self):
        return self.code
