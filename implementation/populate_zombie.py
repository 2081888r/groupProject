import os
import datetime
from random import randint
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'groupProject.settings')

import django
django.setup()
from django.contrib.auth.models import User
from zombie.models import UserProfile, Score
                     
                                   

                                   
                                   

def addUser(name, pw, email, is_staff, is_superuser, is_active): 
    user = User.objects.get_or_create(username = name,
                                      password =pw,
                                      email = email,
                                      is_staff = is_staff,
                                      is_superuser = is_superuser,
                                      is_active = is_active,)[0]
    return user


def addUserProfile(user, avatar, friends, killer, survivor, gatherer, people,explorer,noob):
    UserProfile.objects.get_or_create(user=user, 
                                      avatar=avatar
                                      friends = friends
                                      has_killer_badge = killer
                                      has_survivor_badge = survivor
                                      has_gatherer_badge = gatherer
                                      has_people_person_badge = people
                                      has_explorer_badge = explorer
                                      has_noob_badge =noob
                                      )[0]
    
def addScores(user,days,kills,survivors):
    Score.objects.get_or_create(user = user
                                days_survived = days
                                zombie_kills = kills
                                most_survivors = survivors)[0]


def populate():

 
    
    
    #populate users
    print "Adding users..."
    admin = User.objects.get(username = "test")
    jill = addUser("jill", "jill", "jill@2081888R.gla.ac.uk", False, False, True)
    bob = addUser("bob", "bob", "bob@2081888R.gla.ac.uk", False, False, True)
    jen = addUser("jen", "jen", "jen@2081888R.gla.ac.uk", False, False, True)
    print "Added users!"
    print
    
    #populate userprofiles

    ##  TODO  ADD FRIENDS INITIALISATION
    print "Adding profiles..."
    addUserProfile(admin,  "profile_images/cage.jpg",[] , true, true, true, true, true, true)
    addUserProfile(jill,  "profile_images/cage1.jpg", [], false, false, false, false, false, false)
    addUserProfile(bob, "profile_images/cage2.jpg", [], false, false, false, false, false, false)
    addUserProfile(jen,  "profile_images/cage3.jpg", [], false, false, false, false, false, false)
    print "Added profiles!"
    print 
  
    
    
  
    
    print "Adding scores..."
    addScores(admin,9999,9999,9999)
    addScores(jill,0,0,0)
    addScores(bob,0,0,0)
    addScores(jen,0,0,0)
    print "Added scores!"
    print



if __name__ == '__main__':
    print "Please wait - Infecting world..."
    populate()
