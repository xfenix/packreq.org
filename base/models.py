from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext as _


class Language(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    slug = models.SlugField(max_length=255, verbose_name=_('Alias'), unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(
                self.title\
                    .replace('+', '-plus')\
                    .replace('#', '-sharp'))
            if len(self.slug) < 3:
                self.slug += 'lang'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pk',]
        verbose_name = _('Programming language')
        verbose_name_plural = _('Programming languages')


class PackageRequest(models.Model):
    LEVEL_ELEMENTARY = 0
    LEVEL_EASY = 1
    LEVEL_MEDIUM = 2
    LEVEL_HARD = 3
    LEVEL_NIGHTMARE = 4
    LEVELS = (
        (LEVEL_ELEMENTARY, _('Elementary')),
        (LEVEL_EASY, _('Easy')),
        (LEVEL_MEDIUM, _('Medium')),
        (LEVEL_HARD, _('Hard')),
        (LEVEL_NIGHTMARE, _('Nightmare')),
    )
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    language = models.ForeignKey('Language', verbose_name=_('Language'), on_delete=models.PROTECT)
    description = models.TextField(verbose_name=_('Description'))
    level = models.IntegerField(choices=LEVELS, default=LEVEL_EASY)
    rating = models.DecimalField(verbose_name=_('Rating '), max_digits=12, decimal_places=2)
