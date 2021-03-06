from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from zombie.forms import UserForm, UserProfileForm, ImageUploadForm
from django.contrib.auth.models import User
from zombie.models import UserProfile, Score
import re
import os.path
from engine.game import Game, PlayerState
import pickle
import dill

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
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
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
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.set_password(password1)
            user.save();
            
            user_profile = UserProfile.objects.create(user=user)
            user_profile.save();
            return render(request,'zombie/index.html', {'registration_successful':True})
    else:
        return redirect("/zombie/")

def leaderboard(request):
    if request.method == 'POST':
        if request.POST.get('sort_by') == 'days_survived':
            scores = Score.objects.order_by('-days_survived')[:10]
            scores_sorted_by = "days_survived"
        elif request.POST.get('sort_by') == 'zombie_kills':
            scores = Score.objects.order_by('-zombie_kills')[:10]
            scores_sorted_by = "zombie_kills"
        elif request.POST.get('sort_by') == 'most_survivors':
            scores = Score.objects.order_by('-most_survivors')[:10]
            scores_sorted_by = "most_survivors"
        else:
            scores = Score.objects.order_by('-days_survived')[:10]
            scores_sorted_by = "days_survived"
    else:
        scores = Score.objects.order_by('-days_survived')[:10]
        scores_sorted_by = "days_survived"
    context_dict = {
        'scores':scores,
        'scores_sorted_by':scores_sorted_by
    }
    return render(request, 'zombie/leaderboard.html', context_dict)

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
            
            form = ImageUploadForm(request.POST, request.FILES)
            if form.is_valid():
                user_profile.avatar = form.cleaned_data['new_profile_pic']
                user_profile.save()
            
            if request.POST.get("friend_username") is not None: #adding friend
                friend_username = request.POST.get("friend_username")
                friend_profile = UserProfile.objects.get(user=User.objects.get(username=friend_username))
                user_profile.friends.add(friend_profile)
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


def game(request):
    if request.POST.get("is_new_game") == "yes":
        g = Game()
    else:
        if not os.path.isfile('gameData/'+request.user.username+'.txt'): #new game
            g = Game()
        else: #continue game
            f = open('gameData/'+request.user.username+'.txt', 'rb')
            g = dill.load(f)
            f.close()
    
    
    if g.game_state is None: #game is uninitialised
        g.start_new_day()
    
    #update max_party
    if g.update_state.party >0:
        g.player_state.max_party += g.update_state.party
    
    new_day = False
    
    if g.is_day_over():
        new_day = True
        g.start_new_day()
    
    if request.method == 'POST':
        print "-------------------------"
        print request.POST.get('action')
        print request.POST.get('pos')
        print "-------------------------"
        action = request.POST.get('action')
        if action == 'MOVEENTER':
            pos = request.POST.get('pos')
            g.take_turn('MOVE', int(pos))
            g.take_turn('ENTER')
        elif action == 'SEARCH':
            pos = request.POST.get('pos')
            g.take_turn(action, int(pos))
        else:
            g.take_turn(action)
    
    if g.is_game_over():
        days_survived = g.player_state.days
        zombie_kills = g.player_state.kills
        most_survivors = g.player_state.max_party
        user_prof = UserProfile.objects.get(user=request.user)
        
        score = Score.objects.create(user=user_prof, zombie_kills=zombie_kills, most_survivors=most_survivors, days_survived=days_survived)
        score.save()
        
        os.remove('gameData/'+request.user.username+'.txt')
        
        return render(request, "zombie/gamedeath.html", {'days_survived':days_survived, 'zombie_kills':zombie_kills, 'most_survivors':most_survivors})
    
    f = open('gameData/'+request.user.username+'.txt', 'wb')
    dill.dump(g, f)
    f.close()
    
    t = str(int(((84-g.time_left)/6)+10))+":"+str(int((84-g.time_left)%6))+"0";
    
    return render(request, 'zombie/game.html', {'game':g, 'time':t, 'new_day':new_day})