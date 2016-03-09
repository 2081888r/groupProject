from django.contrib import admin

from cocktail.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ( 'full_name', 'avatar')

class Admin(admin.ModelAdmin):
    list_display = ( 'ID', 'name')

admin.site.register(UserProfile, Admin)