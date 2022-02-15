from multiprocessing import context

from django.contrib import messages
# add authenticate and login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import HttpResponse, redirect, render

from users.models import Profile, User

from .forms import ProfileForm, UpdateUserForm, UserForm

# Create your views here.


def register(request):
    form = UserForm()

    if request.method == 'POST':
        # pass in post data when instantiate the form.
        
        
        form = UserForm(request.POST, request.FILES)
        # if the form is ok with the info filled:
        if form.is_valid():
            form.save()
            # that creates a new user
            # after creation of the user, want to authenticate it
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # inspect the page and see the first password is password1, import authenticate
            user = authenticate(username=username, password=password)

            # want user to login right after registered, import login
            messages.success(request, "Register successfull")
            login(request, user)
            # want to redirect to home page, import redirect
            return redirect('home')

    context = {
        'form_user': form
    }

    return render(request, "users/register.html", context)


@login_required
def user_logout(request):
    messages.success(request, "You Logout!")
    logout(request)
    return redirect('home')


def user_login(request):

    form = AuthenticationForm(request, data=request.POST)

    if form.is_valid():
        user = form.get_user()
        if user:
            messages.success(request, "Login successfull")
            login(request, user)
            return redirect('home')
    return render(request, 'users/login.html', {"form": form})


@login_required
def user_profile(request):
    print(request)

    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(
            request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('home')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'users/profile.html', context)
