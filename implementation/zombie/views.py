from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from zombie.forms import UserForm, UserProfileForm
from django.contrib.auth.models import User
from zombie.models import UserProfile, Score
import re;

#Extra/helper functions here

def getUser(request, username):
    user = User.objects.get(username = username)
   
    return 

#Create your views here.

def index(request):
    if(request.user.is_authenticated()):
        return render(request,'zombie/main.html', {'username':request.user.username})
    else:
        return render(request,'zombie/index.html', {})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/zombie/')
            else:
                return HttpResponse("Your Zombie account is disabled.")
        else:
            return render(request, 'zombie/index.html', {'login_errors':True});
    else:
        return redirect("/zombie/")
    
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/zombie/')

def register(request):
    if request.method == 'POST':
        any_errors = False #true if any error occured
        errors = [False, False, False, False] #lists errors (username_taken, username_invalid, email_invalid, passwords_mismatch)
        
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if(User.objects.filter(username=username).exists()): #if username is taken
            errors[0] = True
            any_errors = True
        if(not re.compile(r'^[a-z0-9]+$').match(username)): #if username does not contain only lowercase letters and numbers
            errors[1] = True
            any_errors = True;
        if(not re.compile(r'^[a-zA-Z0-9\!\#\$\%\&\'\*\+\-\/\=\?\^\_\`\{\|\}\~\.]+@[a-zA-Z\-\.]+\.[a-zA-Z\-\.]+$').match(email)): #if email is invalid (see https://en.wikipedia.org/wiki/Email_address#Syntax)
            errors[2] = True
            any_errors = True
        if(password1 != password2): #if passwords don't match
            errors[3] = True
            any_errors = True
        
        if(any_errors):
            return render(request, 'zombie/index.html', {'errors':errors, 'registration_errors':any_errors});
        else:
            user = User.objects.create_user(username)
            user.email = email
            user.set_password(password1)
            user.save();
            return render(request,'zombie/index.html', {'registration_successful':True})
    else:
        return redirect("/zombie/")

def profile(request, username):
    try:
        user = User.objects.get(username = username)
        user_profile = UserProfile.objects.get(user=user)
        
        if request.method == 'POST':
            if request.POST.get('sort_by') == 'days_survived':
                scores = Score.objects.filter(user__exact=user_profile).order_by('-days_survived')
                scores_sorted_by = "days_survived"
            elif request.POST.get('sort_by') == 'zombie_kills':
                scores = Score.objects.filter(user__exact=user_profile).order_by('-zombie_kills')
                scores_sorted_by = "zombie_kills"
            elif request.POST.get('sort_by') == 'most_survivors':
                scores = Score.objects.filter(user__exact=user_profile).order_by('-most_survivors')
                scores_sorted_by = "most_survivors"
            else:
                scores = Score.objects.filter(user__exact=user_profile).order_by('-days_survived')
                scores_sorted_by = "days_survived"
        else:
            scores = Score.objects.filter(user__exact=user_profile).order_by('-days_survived')
            scores_sorted_by = "days_survived"
        
        context_dict = {
            'username':user.username,
            'first_name':user.first_name,
            'last_name':user.last_name,
            'user_avatar':user_profile.avatar,
            'friends':user_profile.friends.all(),
            'killer_badge_unlocked':user_profile.has_killer_badge,
            'survivor_badge_unlocked':user_profile.has_survivor_badge,
            'gatherer_badge_unlocked':user_profile.has_gatherer_badge,
            'people_person_badge_unlocked':user_profile.has_people_person_badge,
            'explorer_badge_unlocked':user_profile.has_explorer_badge,
            'noob_badge_unlocked':user_profile.has_noob_badge,
            'scores':scores,
            'scores_sorted_by':scores_sorted_by
        }
        
        return render(request, 'zombie/profile.html', context_dict)
    except User.DoesNotExist as u:
        print '%s (%s)' % (u.message, type(u))
        return redirect("/zombie/404/")

def friends(request, username):
    try:
        user = User.objects.get(username = username)
        user_profile = UserProfile.objects.get(user=user)
        
        context_dict = {
            'username':user.username,
            'first_name':user.first_name,
            'last_name':user.last_name,
            'friends':user_profile.friends.all()
        }
        
        return render(request, 'zombie/friends.html', context_dict)
    except User.DoesNotExist as u:
        print '%s (%s)' % (u.message, type(u))
        return redirect("/zombie/404/")

def badges(request, username):
    try:
        user = User.objects.get(username = username)
        user_profile = UserProfile.objects.get(user=user)
        
        context_dict = {
            'username':user.username,
            'first_name':user.first_name,
            'last_name':user.last_name,
            'killer_badge_unlocked':user_profile.has_killer_badge,
            'survivor_badge_unlocked':user_profile.has_survivor_badge,
            'gatherer_badge_unlocked':user_profile.has_gatherer_badge,
            'people_person_badge_unlocked':user_profile.has_people_person_badge,
            'explorer_badge_unlocked':user_profile.has_explorer_badge,
            'noob_badge_unlocked':user_profile.has_noob_badge,
        }
        
        return render(request, 'zombie/badges.html', context_dict)
    except User.DoesNotExist as u:
        print '%s (%s)' % (u.message, type(u))
        return redirect("/zombie/404/")