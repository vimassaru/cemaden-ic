from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class UserRole(models.Model):
    id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.id} - {self.role}'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(UserRole, on_delete=models.SET_NULL, null=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.user.username


class School(models.Model):
    id = models.AutoField(primary_key=True)
    entity_code = models.CharField(max_length=10)
    school_name = models.CharField(max_length=255)
    uf_code = models.CharField(max_length=2)
    uf = models.CharField(max_length=2)
    town_code = models.CharField(max_length=10)
    town_name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.entity_code} - {self.school_name}'


class Cobrade(models.Model):
    id = models.AutoField(primary_key=True)
    cobrade_id = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.cobrade_id} - {self.description}'


class SchoolForm(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(default=timezone.now)
    statusForm = models.CharField(max_length=50, default='Criado')
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    school = models.ForeignKey('School', on_delete=models.CASCADE)
    cobrade_id = models.ForeignKey('Cobrade', on_delete=models.CASCADE)
    cobrade_detail = models.CharField(max_length=255, blank=True)
    initial_date = models.DateField()
    final_date = models.DateField(blank=True, null=True)
    id_fide = models.CharField(max_length=20, blank=True)
    age_range_form = models.JSONField(blank=True, null=True)
    genero = models.CharField(max_length=50, blank=True)
    raca = models.CharField(max_length=50, blank=True)
    escolaridade = models.CharField(max_length=50, blank=True)
    tipos_danos = models.JSONField(blank=True, null=True)
    qtd_alunos_mortos = models.CharField(max_length=50, blank=True)
    qtd_alunos_feridos = models.CharField(max_length=50, blank=True)
    qtd_alunos_desalojados = models.CharField(max_length=50, blank=True)
    qtd_alunos_desabrigados = models.CharField(max_length=50, blank=True)
    qtd_alunos_doentes = models.CharField(max_length=50, blank=True)
    qtd_alunos_traumas_psicologicos = models.CharField(
        max_length=50, blank=True)
    qtd_servidores_mortos = models.CharField(max_length=50, blank=True)
    qtd_servidores_feridos = models.CharField(max_length=50, blank=True)
    qtd_servidores_desalojados = models.CharField(max_length=50, blank=True)
    qtd_servidores_desabrigados = models.CharField(max_length=50, blank=True)
    qtd_servidores_doentes = models.CharField(max_length=50, blank=True)
    qtd_servidores_traumas_psicologicos = models.CharField(
        max_length=50, blank=True)
    suggestions = models.TextField(blank=True, null=True)
    # Repita para os outros campos...

    def __str__(self):
        return f'Formulário {self.id} - {self.suggestions}'
