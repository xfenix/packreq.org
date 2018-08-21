from django.db import models
from django.utils.translation import gettext as _


class Language(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    slug = models.SlugField(max_length=255, verbose_name=_('Alias'))

    class Meta:
        ordering = ['-pk',]
        verbose_name = _('Programming language')
        verbose_name_plural = _('Programming languages')


class PackageRequest(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    language = models.ForeignKey('Language', verbose_name=_('Language'), on_delete=models.PROTECT)
