# flake8: noqa
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import SchoolForm, CustomUserCreationForm, UserProfile, UserRole

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
            # Redireciona para o perfil do usuário ou outra página
            return redirect('user_profile')
        else:
            # Mensagem de erro
            messages.error(request, "Nome de usuário ou senha incorretos.")
    return render(request, 'website/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')


@login_required  # Garante que o usuário esteja autenticado
def register(request):
    # Verifica se o usuário atual é staff
    if not request.user.is_staff:
        messages.error(
            request, "Você não tem permissão para registrar novos usuários.")
        # Redireciona para a página de login ou outra página
        return redirect('login')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_superuser = False  # Garante que o usuário não seja super admin
            user.is_staff = False       # Garante que o usuário não tenha acesso ao admin
            user.save()                 # Salva o usuário no banco de dados

            # Atribui o papel padrão "Registradores"
            registrador_role = UserRole.objects.get(
                pk=2)  # ID para "Registradores"
            UserProfile.objects.create(user=user, role=registrador_role)

            messages.success(
                request, "Registro realizado com sucesso! Você pode fazer login agora.")
            return redirect('login')
        else:
            # Adicione esta linha para verificar os erros no console
            print(form.errors)
    else:
        form = CustomUserCreationForm()

    return render(request, 'website/register.html', {'form': form})


def form_view(request):
    return render(request, 'website/form.html')


@login_required
def user_profile(request):
    return render(request, 'website/user_profile.html')


@login_required
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
