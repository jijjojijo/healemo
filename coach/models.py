from django.db import models
from django.utils.translation import gettext_lazy as _


class Coach(models.Model):
    """Quiz model"""
    name = models.CharField(_('name'), max_length=255)
    description = models.TextField(_('description'))
    image = models.ImageField(_('image'), upload_to='quiz/')
    draft = models.BooleanField(_('draft'), default=False)

    def __str__(self):
        return self.name
