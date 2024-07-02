from django.shortcuts import render, redirect
from users.models import UserProfile
from users.forms import LoginForm, SignUpForm

from django.contrib import auth, messages
from django.contrib.auth.models import User


def login(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('lessons')

            else:
                messages.error(request, "Invalid username or password")
                return redirect('signup')
    else:
        form = LoginForm()

    return render(request, "users/login.html", {'form': form})


def logout(request):
    auth.logout(request)
    messages.success(request, "Logout successfully")
    return render(request, "base.html")


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)

        if form.is_valid():

            try:
                user = User.objects.get(email=request.POST['email'])
                if user:
                    messages.error(request, 'This Email already exists!')
                    return render(request, 'users/signup.html')

            except User.DoesNotExist:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1'],
                    email=request.POST['email']
                )
                auth.login(request, user)
                user_profile = UserProfile.objects.create(
                    user=user,
                    #profile_picture=form['profile_picture']
                )
                user_profile.save()
                return redirect('lessons')

    else:
        form = SignUpForm()

    return render(request, 'users/signup.html', {'form': form})


