from django.shortcuts import render, redirect
from users.forms import LoginForm, UserForm, UserProfileForm, PhoneNumberFormSet

from django.contrib import auth, messages
from django.contrib.auth.models import User

from users.models import UserProfile, PhoneNumber


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
    extra_forms = int(request.GET.get('extra', 1))  # Ensure extra_forms is an integer

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        number_formset = PhoneNumberFormSet(request.POST, queryset=PhoneNumber.objects.none())

        if user_form.is_valid() and profile_form.is_valid() and number_formset.is_valid():
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
                print(number_formset)

                for number_form in number_formset:
                    if number_form.cleaned_data:
                        phone_number = number_form.save(commit=False)
                        phone_number.user = user
                        phone_number.save()

                auth.login(request, user)
                return redirect('lessons')

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
        number_formset = PhoneNumberFormSet(queryset=PhoneNumber.objects.none())

    return render(request, 'users/signup.html', {'user_form': user_form,
                                                 'profile_form': profile_form,
                                                 'number_formset': number_formset,
                                                 'extra_forms': extra_forms}
                  )


