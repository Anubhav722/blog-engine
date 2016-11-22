from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.conf import settings

class Content(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title=models.CharField(max_length=120)
     
    def __unicode__(self):
        return self.title
        
class Content_Types(models.Model):
    
    content=models.ForeignKey(Content)
    descripton=models.TextField(null=True, blank=True)
    image=models.ImageField(null=True, blank=True)
    video=models.FileField(default='')
    
    def __unicode__(self):
        return self.descripton