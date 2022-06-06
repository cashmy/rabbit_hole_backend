from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('name'))
    description = models.TextField(verbose_name=_('description'), blank=True)
    owner = models.ForeignKey('auth.User', related_name='projects', on_delete=models.CASCADE)
    # theme_color = models.CharField(max_length=50, verbose_name=_('theme_color'))
    archived = models.BooleanField(default=False, verbose_name=_('archived'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated_at'))

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.name
    