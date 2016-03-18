from django.contrib import admin

from zombie.models import UserProfile
from zombie.models import Score

admin.site.register(UserProfile)
admin.site.register(Score)