from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import profile_form
from django.conf import settings
import os

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('IndexView')
        else:
            return render(request, 'accounts/login.html', {'error' : 'username or password is in correct'})
    return render(request, 'accounts/login.html')

def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username = request.POST["username"], password= request.POST["password1"])
            auth.login(request,user)
        return redirect('IndexView')
    return render(request, 'accounts/signup.html')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('IndexView')

@login_required
def profile(request, pk):
    profile = get_object_or_404(User, pk=pk)
    return render(request, 'accounts/profile.html', {'profile_user' : profile})

 

@login_required
def update_profile(request, pk):
    profile = get_object_or_404(User, pk=pk)
    print(profile.profile.name)
    if request.method == "POST":
        form = profile_form(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            profile.profile.name = form.cleaned_data['name']
            profile.profile.address = form.cleaned_data['address']
            profile.profile.profile_photo = form.cleaned_data['profile_photo']
            print(profile.profile.profile_photo)
            imgfile = settings.MEDIA_ROOT+ "/" + str(pk) + "/" + str(pk)
            print(imgfile)
            try:
                os.remove(imgfile)
            except:
                pass
            profile.profile.save()
            return redirect('profile', pk=pk)
    else :
        form = profile_form(instance=profile.profile)
    return render(request, 'accounts/update_profile.html', {'form' : form})
