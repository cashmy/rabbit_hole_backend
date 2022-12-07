from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Solution(models.Model):
    type = models.CharField(max_length=10, verbose_name=_('Solution Type')) # Types are s=soluion, r=redirect/re-focus
    description = models.TextField(max_length=255, verbose_name=_('description'), blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated_at'))

    class Meta:
        verbose_name = _('Solution')
        verbose_name_plural = _('Solutions')
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.description[0:25]