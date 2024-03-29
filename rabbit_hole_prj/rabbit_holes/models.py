from django.db import models
from projects.models import Project
from solutions.models import Solution
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Rabbit_Hole(models.Model):
    project = models.ForeignKey(Project, related_name='projects', on_delete=models.CASCADE)
    log_type = models.CharField(max_length=10, verbose_name=_('Log Type')) # d=distraction, i=impediment, t=task
    name = models.CharField(max_length=50, verbose_name=_('name'))
    description = models.TextField(verbose_name=_('description'), blank=True)
    rating = models.IntegerField(default=0, verbose_name=_('rating'))
    solution = models.ForeignKey(Solution,  
                                 null=True, 
                                 blank=True,
                                 on_delete=models.SET_NULL)
    completed = models.BooleanField(default=False, verbose_name=_('completed'))
    archived = models.BooleanField(default=False, verbose_name=_('archived'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated_at'))

    class Meta:
        verbose_name = _('Rabit Hole')
        verbose_name_plural = _('Rabbit Holes')
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.name