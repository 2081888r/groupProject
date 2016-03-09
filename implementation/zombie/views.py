from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from zombie.forms import UserForm, UserProfileForm
from django.contrib.auth.models import User
from zombie.models import UserProfile

#Extra/helper functions here!

def getUser(request, username):
    user = User.objects.get(username = username)
   
    return 



# Create your views here.

def index(request):
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
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request,'registration/login.html', {})
    
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/zombie/')

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print user_form.errors

    else:
        user_form = UserForm()

    return render(request, 'registration/registration_form.html', {'user_form': user_form, 'registered': registered} )
    
@login_required
def register_profile(request):
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES) #get the data and the files from the form
        
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user     #get the user we want to update the profile
            profile.save()  #save the profile
            return HttpResponseRedirect('/zombie/')  #redirect to the homepage
        else:
            print profile_form.errors   
    else:
        profile_form = UserProfileForm()
    
    return render(request,"profiles/profile_update.html", {'profile_form': profile_form, 'user_name': request.user})


def profile(request, username):
    try:
        user = User.objects.get(username = username)
        profile = UserProfile.objects.get(user_id = user.id)
        return render(request,"profiles/profile.html", {'player': user, 'profile': profile})
    except User.DoesNotExist as u:
        print '%s (%s)' % (u.message, type(u))
        return HttpResponseRedirect('/zombie/404/')  #if user doesn't exist
    except Exception as e:
        print '%s (%s)' % (e.message, type(e))
        return HttpResponseRedirect('/zombie/404/')  #catch all the exceptions
    
@login_required
def profile_update(request):
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES)
        if profile_form.is_valid():
            profile = UserProfile.objects.get(user_id = request.user.id)
            profile_form_data = profile_form.cleaned_data
            profile_new_avatar = profile_form_data['avatar']
            profile_new_full_name = profile_form_data['full_name']
            if profile_new_avatar is not None: 
                profile.avatar = profile_new_avatar
            if len(profile_new_full_name) > 0: 
                profile.full_name = profile_new_full_name
                print profile_new_full_name
            profile.save()
            url = '/zombie/profile/'+str(request.user.username)
            return HttpResponseRedirect(url)  #redirect to the profile
        else:
            print profile_form.errors
#             
    else:
        profile_form = UserProfileForm()
    
    return render(request,"profiles/profile_update.html", {'profile_form': profile_form, 'user_name': request.user})
    
    
def error_page(request):
    return render(request, 'zombie/404.html')
