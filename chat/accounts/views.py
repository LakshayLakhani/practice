from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import LoginForm, SignUpForm
from .models import UserDetails
from .utils import create_username

def login_user(request):

    if request.user.is_authenticated():
        return redirect("group")

    # email = request.GET.get('email', '')

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            profile_obj = UserDetails.objects.get(user__email=email)
            username = profile_obj.user.username
            user = authenticate(username=username, password=form.cleaned_data['password'])
            if user:
                if user.is_active:
                    login(request, user)

                    return redirect('main_home')

        return render(request, 'login.html', {'form':form})

    else:
        form = LoginForm(request.POST or None )
        return render(request, 'login.html', {"form":form})

@login_required
def user_logout(request):
    """
        Function is used to logout the user from the day planner.
    """

    logout(request)
    return redirect("login")

def Signup(request):
    if request.user.is_authenticated():
        return redirect('group')

    form = SignUpForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = User.objects.create_user(
                username=create_username('%s %s' % (form.cleaned_data["first_name"], form.cleaned_data["last_name"])),
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                is_active = True,
            )
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()

            UserDetail = UserDetails.objects.create(
            user=user
            )
            return redirect('login')
    else:
        form = SignUpForm()

    return render(request, "signup.html", {
        "form":form,
        })

# def details(request):
#     form = UserDetailsForm(request.POST or None)
#     return render(request, "details.html", {})
