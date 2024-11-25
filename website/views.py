# flake8: noqa
import csv
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .forms import SchoolForm, CustomUserCreationForm, UserProfile, UserRole

from .models import SchoolForm as SchoolFormModel

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


@user_passes_test(lambda u: u.is_staff)
@login_required
def suggestion_list(request):
    # Obtendo todas as instâncias de SchoolForm
    school_forms = SchoolFormModel.objects.all()

    if request.method == 'POST':
        # Lógica para exportar como CSV
        response = HttpResponse(content_type='text/csv')

        # Gerar nome de arquivo dinâmico com a data atual
        current_date = datetime.now().strftime('%d_%m_%Y')  # Formato dia_mês_ano
        filename = f'sugestoes_{current_date}.csv'  # Nome do arquivo

        response['Content-Disposition'] = f'attachment; filename="{filename}"'

        writer = csv.writer(response)
        # Cabeçalho da planilha
        writer.writerow(['Data de Criação', 'Usuário', 'Escola', 'Sugestão'])

        for form in school_forms:
            created_at = form.created_at.strftime(
                '%d/%m/%Y') if form.created_at else '-'
            user_name = form.user.username if form.user else 'Anônimo'
            # Exibe '-' se suggestions for None ou vazia
            suggestion_text = form.suggestions if form.suggestions else '-'

            writer.writerow([
                created_at,
                user_name,
                str(form.school),
                suggestion_text  # Usando a variável suggestion_text
            ])

        return response

    return render(request, 'website/suggestion_list.html', {'school_forms': school_forms})
