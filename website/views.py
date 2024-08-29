# flake8: noqa
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import SchoolForm

# Create your views here.


def home(request):
    return render(request, 'website/home.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_profile')
    return render(request, 'website/login.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'website/register.html', {'form': form})


def form_view(request):
    return render(request, 'website/form.html')


@login_required
def user_profile(request):
    return render(request, 'website/user_profile.html')


def school_form_view(request):

    if request.method == 'POST':
        print(request.user.email)
        form = SchoolForm(request.POST)

        if form.is_valid():
            school_form = form.save(commit=False)
            school_form.user = request.user
            school_form.save()  # Salve os dados no banco de dados

            return redirect('form_success')
        else:
            print(form.errors)
    else:
        form = SchoolForm()

    return render(
        request, 'website/school_form.html', {'form': form}
    )


def form_success(request):
    return render(request, 'website/form_success.html')
