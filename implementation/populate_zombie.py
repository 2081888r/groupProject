import os
import datetime
from django.db import IntegrityError
from random import randint
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'groupProject.settings')

import django
django.setup()
from django.contrib.auth.models import User
from zombie.models import UserProfile, Score

def addUser(name, pw, email, first_name, last_name):
    try:
        user = User.objects.create_user(
            username = name,
            password = pw,
            email = email,
            first_name = first_name,
            last_name = last_name,
        )
        return user
    except IntegrityError:
        user = User.objects.get(username=name)
        user.set_password(pw)
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        return user

def addUserProfile(user, avatar, friends, killer, survivor, gatherer, people,explorer,noob):
    user_prof = UserProfile.objects.get_or_create(
        user = user, 
        avatar = avatar,
        has_killer_badge = killer,
        has_survivor_badge = survivor,
        has_gatherer_badge = gatherer,
        has_people_person_badge = people,
        has_explorer_badge = explorer,
        has_noob_badge = noob
    )[0]
    user_prof.friends.add(*friends)
    return user_prof
    
def addScores(user,days,kills,survivors):
    Score.objects.get_or_create(
        user = user,
        days_survived = days,
        zombie_kills = kills,
        most_survivors = survivors
    )[0]


def populate():
    #populate users
    print "Adding users..."
    jill = addUser("jill", "jill", "jill@fake.ac.uk", "Jill", "Pickle")
    bob = addUser("bob", "bob", "bob@fake.co.uk", "Bob", "Smith")
    jen = addUser("jen", "jen", "jen@fake.com", "Jen", "Cunningham")
    print "Added users!"
    print
    
    #populate userprofiles
    print "Adding profiles..."
    jill_prof = addUserProfile(jill,  "", [], True, False, True, True, False, True)
    bob_prof = addUserProfile(bob, "", [jill_prof], False, True, True, True, False, False)
    jen_prof = addUserProfile(jen,  "", [jill_prof, bob_prof], True, True, True, True, True, True)
    print "Added profiles!"
    print 
    
    
    
    #populate scores
    print "Adding scores..."
    addScores(jill_prof,5,10,9)
    addScores(jill_prof,4,11,10)
    addScores(jill_prof,3,9,8)
    addScores(jill_prof,4,12,5)
    addScores(jill_prof,3,12,5)
    addScores(jill_prof,4,12,6)
    addScores(jill_prof,4,11,15)
    addScores(jill_prof,3,10,14)
    addScores(jill_prof,2,12,14)
    
    addScores(bob_prof,5,10,9)
    addScores(bob_prof,4,11,10)
    addScores(bob_prof,3,9,8)
    addScores(bob_prof,4,12,5)
    addScores(bob_prof,3,12,5)
    addScores(bob_prof,4,12,6)
    addScores(bob_prof,4,11,15)
    addScores(bob_prof,3,10,14)
    addScores(bob_prof,2,12,14)
    
    addScores(jen_prof,5,10,9)
    addScores(jen_prof,4,11,10)
    addScores(jen_prof,3,9,8)
    addScores(jen_prof,4,12,5)
    addScores(jen_prof,3,12,5)
    addScores(jen_prof,4,12,6)
    addScores(jen_prof,4,11,15)
    addScores(jen_prof,3,10,14)
    addScores(jen_prof,2,12,14)
    print "Added scores!"
    print

if __name__ == '__main__':
    print "Please wait - Infecting world..."
    populate()
