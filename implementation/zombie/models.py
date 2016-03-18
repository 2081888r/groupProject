from django.db import models
from django.contrib.auth.models import User
import datetime
from django.template.defaultfilters import default
from django.template.defaultfilters import slugify
from django.db.models.fields.related import ForeignKey

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(upload_to='profile_images', blank=True)
    friends = models.ManyToManyField('self', blank=True)
    
    has_killer_badge = models.BooleanField(default=False)
    has_survivor_badge = models.BooleanField(default=False)
    has_gatherer_badge = models.BooleanField(default=False)
    has_people_person_badge = models.BooleanField(default=False)
    has_explorer_badge = models.BooleanField(default=False)
    has_noob_badge = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
       super(UserProfile, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.user.username

class Score(models.Model):
    user = models.ForeignKey(UserProfile)
    days_survived = models.IntegerField()
    zombie_kills = models.IntegerField()
    most_survivors = models.IntegerField()
    
    def save(self, *args, **kwargs):
       super(Score, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.user.user.username+" - "+str(self.days_survived)+" - "+str(self.zombie_kills)+" - "+str(self.most_survivors)