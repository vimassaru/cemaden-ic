# flake8: noqa
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import School, Cobrade, UserRole, UserProfile, SchoolForm as SchoolFormModel


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ModelChoiceField(
        queryset=UserRole.objects.all(), required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'role')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            # Aqui você pode criar o perfil do usuário se necessário
            UserProfile.objects.create(
                user=user, role=self.cleaned_data['role'])
        return user


class SchoolForm(forms.ModelForm):
    class Meta:
        model = SchoolFormModel
        exclude = ['created_at']  # Exclui o campo created_at do formulário
        fields = '__all__'

    school = forms.ModelChoiceField(
        queryset=School.objects.all(),
        label='Escolha uma escola',
        empty_label='Selecione uma Escola.',
        widget=forms.Select(attrs={'class': 'select'})
    )

    cobrade_id = forms.ModelChoiceField(
        queryset=Cobrade.objects.all(),
        label='Código COBRADE',
        widget=forms.Select(attrs={'class': 'select'})
    )

    cobrade_detail = forms.CharField(label='Detalhes COBRADE', max_length=255, required=False, widget=forms.TextInput(attrs={
        'class': 'input',
        'placeholder': 'Observações adicionais sobre o evento natural'
    }))

    initial_date = forms.DateField(label='Data Inicial', widget=forms.DateInput(attrs={
        'class': 'input',
        'type': 'date'
    }))

    final_date = forms.DateField(label='Data Final', required=False, widget=forms.DateInput(attrs={
        'class': 'input',
        'type': 'date'
    }))

    suggestions = forms.CharField(
        label='Sugestões e Observações',
        widget=forms.Textarea(attrs={
            'class': 'textarea',
            'placeholder': 'Adicione suas sugestões aqui...',
            'rows': 5  # Número de linhas visíveis
        }),
        required=False  # Campo opcional
    )

    statusForm = forms.CharField(label='Status', required=False, max_length=50, widget=forms.TextInput(attrs={
        'class': 'input',
        'readonly': 'readonly',
        'value': 'Criado'
    }))

    id_fide = forms.CharField(
        label='ID FIDE (incluir caso seu município teve reconhecimento de estado de calamidade pública ou situação de emergência)',
        max_length=20,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'input',
                'placeholder': 'Exemplo: SP-F-3546405-12200-20160222'
            }
        )
    )

    age_ranges = [
        ('0-3', '0 a 3 anos'),
        ('4-5', '4 a 5 anos'),
        ('6-10', '6 a 10 anos'),
        ('11-14', '11 a 14 anos'),
        ('18+', '>= 18'),
    ]

    age_range_form = forms.MultipleChoiceField(
        label='Faixa Etária',
        required=False,
        choices=age_ranges,
        # Usar checkboxes para múltipla escolha
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox'}),
    )

    genero = forms.ChoiceField(
        label='Gênero',
        choices=[
            ('masculino', 'Masculino'),
            ('feminino', 'Feminino'),
            ('outro', 'Outro'),
            ('nao_informado', 'Não Informado'),
        ],
        required=False,
    )

    raca = forms.ChoiceField(
        label='Raça',
        choices=[
            ('branca', 'Branca'),
            ('preta', 'Preta'),
            ('parda', 'Parda'),
            ('amarela', 'Amarela'),
            ('indigena', 'Indígena'),
            ('nao_informada', 'Não Informada'),
        ],
        required=False,
    )

    escolaridade = forms.ChoiceField(
        label='Escolaridade',
        choices=[
            ('creche', 'Creche'),
            ('pre_escolar', 'Pré-escolar'),
            ('fundamental_iniciais', 'Fundamental - Anos Iniciais'),
            ('fundamental_finais', 'Fundamental - Anos Finais'),
            ('medio', 'Médio'),
            ('educacao_jovens_adultos', 'Educação Jovens Adultos'),
        ],
        required=False,
    )

    tipos_danos = forms.MultipleChoiceField(
        label='Tipos de Danos',
        choices=[
            ('mortos', 'Mortos'),
            ('feridos', 'Feridos'),
            ('desalojados', 'Desalojados'),
            ('desabrigados', 'Desabrigados'),
            ('deslocados', 'Deslocados'),
            ('doentes', 'Doentes'),
            ('traumas_psicologicos', 'Traumas Psicológicos'),
        ],
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox'}),
    )

    qtd_alunos_mortos = forms.CharField(
        label='Quantidade de Mortos',
        required=False,
        help_text='Se não souber, escreva "não sabe".',
        widget=forms.TextInput(attrs={'class': 'input'}),
    )

    qtd_alunos_feridos = forms.CharField(
        label='Quantidade de Feridos',
        required=False,
        help_text='Se não souber, escreva "não sabe".',
        widget=forms.TextInput(attrs={'class': 'input'}),
    )

    qtd_alunos_desalojados = forms.CharField(
        label='Quantidade de Desalojados',
        required=False,
        help_text='Se não souber, escreva "não sabe".',
        widget=forms.TextInput(attrs={'class': 'input'}),
    )

    qtd_alunos_desabrigados = forms.CharField(
        label='Quantidade de Desabrigados',
        required=False,
        help_text='Se não souber, escreva "não sabe".',
        widget=forms.TextInput(attrs={'class': 'input'}),
    )

    qtd_alunos_doentes = forms.CharField(
        label='Quantidade de Doentes',
        required=False,
        help_text='Se não souber, escreva "não sabe".',
        widget=forms.TextInput(attrs={'class': 'input'}),
    )

    qtd_alunos_traumas_psicologicos = forms.CharField(
        label='Quantidade com Traumas Psicológicos',
        required=False,
        help_text='Se não souber, escreva "não sabe".',
        widget=forms.TextInput(attrs={'class': 'input'}),
    )

    qtd_servidores_mortos = forms.CharField(
        label='Quantidade de Mortos',
        required=False,
        help_text='Se não souber, escreva "não sabe".',
        widget=forms.TextInput(attrs={'class': 'input'}),
    )

    qtd_servidores_feridos = forms.CharField(
        label='Quantidade de Feridos',
        required=False,
        help_text='Se não souber, escreva "não sabe".',
        widget=forms.TextInput(attrs={'class': 'input'}),
    )

    qtd_servidores_desalojados = forms.CharField(
        label='Quantidade de Desalojados',
        required=False,
        help_text='Se não souber, escreva "não sabe".',
        widget=forms.TextInput(attrs={'class': 'input'}),
    )

    qtd_servidores_desabrigados = forms.CharField(
        label='Quantidade de Desabrigados',
        required=False,
        help_text='Se não souber, escreva "não sabe".',
        widget=forms.TextInput(attrs={'class': 'input'}),
    )

    qtd_servidores_doentes = forms.CharField(
        label='Quantidade de Doentes',
        required=False,
        help_text='Se não souber, escreva "não sabe".',
        widget=forms.TextInput(attrs={'class': 'input'}),
    )

    qtd_servidores_traumas_psicologicos = forms.CharField(
        label='Quantidade com Traumas Psicológicos',
        required=False,
        help_text='Se não souber, escreva "não sabe".',
        widget=forms.TextInput(attrs={'class': 'input'}),
    )

    age_ranges2 = [
        ('18-20', '<= 20'),
        ('21-30', '21 a 30 anos'),
        ('31-40', '31 a 40 anos'),
        ('40-50', '40 a 50 anos'),
        ('50-60', '50 a 60 anos'),
        ('60+', '>= 60'),
    ]

    age_range_form2 = forms.MultipleChoiceField(
        label='Faixa Etária',
        required=False,
        choices=age_ranges2,
        # Usar checkboxes para múltipla escolha
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox'}),
    )

    genero2 = forms.ChoiceField(
        label='Gênero',
        choices=[
            ('masculino', 'Masculino'),
            ('feminino', 'Feminino'),
            ('outro', 'Outro'),
            ('nao_informado', 'Não Informado'),
        ],
        required=False,
    )

    raca2 = forms.ChoiceField(
        label='Raça',
        choices=[
            ('branca', 'Branca'),
            ('preta', 'Preta'),
            ('parda', 'Parda'),
            ('amarela', 'Amarela'),
            ('indigena', 'Indígena'),
            ('nao_informada', 'Não Informada'),
        ],
        required=False,
    )

    cargo_profissional = forms.ChoiceField(
        label='Cargo Profissional',
        choices=[
            ('profissional_gestao',
             'Administrativos (Gestor, Administrador, Secretário, Coordenador)'),
            ('profissional_servicos',
             'Serviços (Serviços Gerais, Alimentação, Segurança)'),
            ('profissional_saude', 'Saúde (Profissional da Saúde, Fonoaudiólogo, Nutricionista, Psicólogo, Assistente Social)'),
            ('pedagogos', 'Pedagogo (a) (Pedagogo, Bibliotecário, Monitor)'),
            ('professores', 'Professor (a)'),
        ],
        required=False,
    )

    tipos_danos2 = forms.MultipleChoiceField(
        label='Tipos de Danos',
        choices=[
            ('mortos', 'Mortos'),
            ('feridos', 'Feridos'),
            ('desalojados', 'Desalojados'),
            ('desabrigados', 'Desabrigados'),
            ('deslocados', 'Deslocados'),
            ('doentes', 'Doentes'),
            ('traumas_psicologicos', 'Traumas Psicológicos'),
        ],
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox'}),
    )

    quantidade_danos2 = forms.CharField(
        label='Quantidade de Danos',
        required=False,
        help_text='Se não souber, escreva "não sabe".',
        widget=forms.TextInput(attrs={'class': 'input'}),
    )

    terreno = forms.ChoiceField(
        label='Impacto direto sobre o terreno onde está localizada a escola',
        choices=[
            ('soterramento_parc_ou_total', 'Soterramento Parcial ou Total'),
            ('afundamento_solo', 'Afundamento do Solo'),
            ('erosao', 'Erosão'),
            ('sedimentacao', 'Sedimentação'),
            ('outro', 'Outro'),  # Fazer usuário escrever sobre o outro
        ],
        required=False,
        widget=forms.Select(attrs={'class': 'select'})
    )

    outro_terreno = forms.CharField(
        label='Descreva o impacto',
        max_length=255,
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'input', 'placeholder': 'Descreva aqui...'})
    )

    infra_fisico = forms.MultipleChoiceField(
        label='Estrutura física',
        choices=[
            ('vigas', 'Vigas'),
            ('colunas', 'Colunas'),
            ('fundacoes', 'Fundações'),
            ('nao_afetado', 'Não Afetado'),
        ],
        required=False,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox'})
    )

    infra_comodos = forms.MultipleChoiceField(
        label='Estrutura dos Comodos',
        choices=[
            ('parades', 'Paredes'),
            ('piso', 'Piso'),
            ('teto', 'Teto'),
            ('nao_afetado', 'Não Afetado'),
        ],
        required=False,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox'})
    )

    infra_eletrica = forms.MultipleChoiceField(
        label='Estrutura Elétrica',
        choices=[
            ('cabeamento', 'Cabeamento'),
            ('interruptures', 'Interruptures'),
            ('tomadas', 'Tomadas'),
            ('lampadas', 'Lâmpadas'),
            ('nao_afetado', 'Não Afetado'),
        ],
        required=False,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox'})
    )

    infra_aqueduto_sanamento = forms.MultipleChoiceField(
        label='Estrutura de Aqueduto e Saneamento',
        choices=[
            ('sis_agua_potavel', 'Sistema de água potável'),
            ('esgoto_sanitario', 'Esgoto Sanitário'),
            ('drenagem_pluvial', 'Drenagem Pluvial'),
            ('nao_afetado', 'Não Afetado'),
        ],
        required=False,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox'})
    )

    eq_computador = forms.CharField(
        label='Perdas de Computadores',
        required=False,
        help_text='Se não souber, escreva "não sabe".',
        widget=forms.TextInput(attrs={'class': 'input'}),
    )

    eq_datashow = forms.CharField(
        label='Perdas de Datashow',
        required=False,
        help_text='Se não souber, escreva "não sabe".',
        widget=forms.TextInput(attrs={'class': 'input'}),
    )

    eq_cadeiras = forms.CharField(
        label='Perdas de Cadeiras',
        required=False,
        help_text='Se não souber, escreva "não sabe".',
        widget=forms.TextInput(attrs={'class': 'input'}),
    )

    eq_mesas = forms.CharField(
        label='Perdas de Mesas',
        required=False,
        help_text='Se não souber, escreva "não sabe".',
        widget=forms.TextInput(attrs={'class': 'input'}),
    )

    eq_ventilador = forms.CharField(
        label='Perdas de Ventiladores',
        required=False,
        help_text='Se não souber, escreva "não sabe".',
        widget=forms.TextInput(attrs={'class': 'input'}),
    )

    eq_ar_condicionado = forms.CharField(
        label='Perdas de Ar Condicionado',
        required=False,
        help_text='Se não souber, escreva "não sabe".',
        widget=forms.TextInput(attrs={'class': 'input'}),
    )

    eq_estantes = forms.CharField(
        label='Perdas de Estantes',
        required=False,
        help_text='Se não souber, escreva "não sabe".',
        widget=forms.TextInput(attrs={'class': 'input'}),
    )

    eq_outros = forms.CharField(
        label='Perdas de Outros Equipamentos Eletrônicos',
        required=False,
        help_text='Se não souber, escreva "não sabe".',
        widget=forms.TextInput(attrs={'class': 'input'}),
    )

    livros = forms.CharField(
        label='Qtd. Livros',
        required=False,
        help_text='Se não souber, escreva "não sabe".',
        widget=forms.TextInput(attrs={'class': 'input'}),
    )

    vidraria = forms.CharField(
        label='Qtd. Vidraria (Tubos, Probetas, etc)',
        required=False,
        help_text='Se não souber, escreva "não sabe".',
        widget=forms.TextInput(attrs={'class': 'input'}),
    )

    eq_medicacao = forms.CharField(
        label='Qtd. Equipamentos de medição',
        required=False,
        help_text='Se não souber, escreva "não sabe".',
        widget=forms.TextInput(attrs={'class': 'input'}),
    )

    eq_outros_materiais = forms.CharField(
        label='Qtd. Outros materiais',
        required=False,
        help_text='Se não souber, escreva "não sabe".',
        widget=forms.TextInput(attrs={'class': 'input'}),
    )

    locais_aprendizado = forms.MultipleChoiceField(
        label='Locais de Aprendizados Afetados',
        choices=[
            ('sala_aula', 'Salas de aula'),
            ('espacos_esportivos', 'Espaços esportivos'),
            ('laboratorios', 'Laboratórios (química, física ou internet)'),
            ('biblioteca', 'Biblioteca'),
            ('nenhum', 'Nenhum'),
        ],
        required=False,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox'})
    )

    locais_convivencia = forms.MultipleChoiceField(
        label='Locais de Convivência Afetados',
        choices=[
            ('sala_reuniao', 'Salas de reunião'),
            ('auditorios', 'Auditórios'),
            ('restaurante', 'Restaurante'),
            ('jardins', 'Jardins'),
            ('nenhum', 'Nenhum'),
        ],
        required=False,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox'})
    )

    dias_sem_aula = forms.CharField(
        label='Quantos Dias Sem Aulas?',
        required=False,
        help_text='Se não souber, escreva "não sabe".',
        widget=forms.TextInput(attrs={'class': 'input'}),
    )

    escola_abrigo = forms.ChoiceField(
        label='Uso da Escola como Abrigo?',
        choices=[
            ('sim', 'Sim'),
            ('nao', 'Não'),
        ],
        required=False,
        widget=forms.Select(attrs={'class': 'select'})
    )

    custo_danos_materiais = forms.CharField(
        label='Custos dos danos materiais',
        required=False,
        help_text='Se não souber, escreva "não sabe".',
        widget=forms.TextInput(attrs={'class': 'input'}),
    )

    custo_atender_emergencia = forms.CharField(
        label='Custos para atender a emergência',
        required=False,
        help_text='Se não souber, escreva "não sabe".',
        widget=forms.TextInput(attrs={'class': 'input'}),
    )

    custo_restaurar_normalidade = forms.CharField(
        label='Custos para restabelecimento da normalidade',
        required=False,
        help_text='Se não souber, escreva "não sabe".',
        widget=forms.TextInput(attrs={'class': 'input'}),
    )

    custo_reparacao = forms.CharField(
        label='Custos de reparação',
        required=False,
        help_text='Se não souber, escreva "não sabe".',
        widget=forms.TextInput(attrs={'class': 'input'}),
    )

    custo_reconstrucao = forms.CharField(
        label='Custos de reconstrução',
        required=False,
        help_text='Se não souber, escreva "não sabe".',
        widget=forms.TextInput(attrs={'class': 'input'}),
    )
