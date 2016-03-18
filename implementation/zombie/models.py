from django.db import models
from django.contrib.auth.models import User
import datetime
from django.template.defaultfilters import default
from django.template.defaultfilters import slugify
from django.db.models.fields.related import ForeignKey

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(upload_to='profile_images', blank=True)
    
    def save(self, *args, **kwargs):
       super(UserProfile, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.user.username
