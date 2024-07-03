from django.shortcuts import render, redirect
from users.forms import LoginForm, UserForm, UserProfileForm

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
            return redirect('login')
    else:
        form = LoginForm()

    return render(request, "users/login.html", {'form': form})


def logout(request):
    auth.logout(request)
    messages.success(request, "Logout successfully")
    return render(request, "base.html")


def signup(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            try:
                user = User.objects.get(email=user_form.cleaned_data['email'])
                if user:
                    messages.error(request, 'This Email already exists!')
                    return render(request, 'users/signup.html')

            except User.DoesNotExist:
                user = user_form.save()
                user_profile = profile_form.save(commit=False)
                user_profile.user = user
                user_profile.save()

                auth.login(request, user)
                return redirect('lessons')

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'users/signup.html', {'user_form': user_form, 'profile_form': profile_form})


