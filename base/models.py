from django.db import models
from .utils import generate_unique_code

SITE_URL = 'http://127.0.0.1:8000/'


class Link(models.Model):
    url = models.URLField(max_length=400)
    code = models.CharField(max_length=6, unique=True, default=generate_unique_code)

    @property
    def short_url(self):
        return SITE_URL + self.code

    def __str__(self):
        return self.code
