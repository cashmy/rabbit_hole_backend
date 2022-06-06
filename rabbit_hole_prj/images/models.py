from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
# Define an "upload to" function in order to store the files/images
# (Note: we wont be able to use the products "id" because the instance 
#  is being created before the data is actually saved.
#  If we want to use the id, we must perform an action after saving)
def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class Image(models.Model):
    file_name = models.ImageField(_("File Name"), upload_to=upload_to, default="images/No_image.png", max_length=255)
    alt_text = models.CharField(_("Alt Text"), max_length=50, blank=True)
    url = models.URLField(_("URL"), max_length=200, blank=True)
    mimeType = models.CharField(_("Mime Type"), max_length=255)
    width = models.IntegerField(_("Width"), blank=True, null=True)
    height = models.IntegerField(_("Height"), blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")

    def __str__(self):
        if self.alt_text != "":
            return self.alt_text
        else:
            return str(self.file_name)
