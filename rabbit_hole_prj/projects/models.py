from django.db import models
from images.models import Image
from authentication.models import User
from django.utils.translation import gettext_lazy as _

class Project(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('name'))
    abbreviation = models.CharField(max_length=10, verbose_name=_('abbreviation'), blank=True)
    description = models.TextField(verbose_name=_('description'), blank=True)
    user = models.ForeignKey(User, 
                             on_delete=models.CASCADE, 
                             blank=True, 
                             null=True)
    text_color = models.CharField(max_length=50, verbose_name=_('text color'), blank=True, default='#000000')     # white
    theme_color = models.CharField(max_length=50, verbose_name=_('theme color'), blank= True, default='#00a2ed')   # blue
    image = models.ForeignKey(Image, on_delete=models.DO_NOTHING, blank=True, null=True, default=1)
    archived = models.BooleanField(default=False, verbose_name=_('archived'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated_at'))

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')
        ordering = ('-name',)
    
    def __str__(self):
        return self.name
    