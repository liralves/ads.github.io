from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import User, Estudante, Professor
from appweb.forms import EstudanteRegistrationForm, ProfessorRegistrationForm
from django.db import IntegrityError

# Home page
def home(request):
    users = User.objects.all()
    return render(request, 'index.html', {"users": users})

# Form page for student registration
def form(request):
    data = {"form": EstudanteRegistrationForm()}
    return render(request, 'form.html', data)

# Page to select the type of registration
def tipo_cadastro(request):
    if request.method == 'POST':
        tipo = request.POST.get('tipo')

        if tipo == 'estudante':
            return redirect('cadastrar_estudante')
        elif tipo == 'professor':
            return redirect('cadastrar_professor')

    return render(request, 'tipo_cadastro.html')

# Function to register a student
def cadastrar_estudante(request):
    if request.method == 'POST':
        form = EstudanteRegistrationForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email_institucional = form.cleaned_data['email_institucional']
            curso = form.cleaned_data['curso']
            periodo = form.cleaned_data['periodo']
            matricula = form.cleaned_data['matricula']
            senha = form.cleaned_data['senha']

            try:
                if User.objects.filter(email=email_institucional).exists():
                    form.add_error('email_institucional', 'Este email já está em uso.')
                else:
                    user = User.objects.create_user(
                        email=email_institucional,
                        password=senha
                    )

                    estudante = Estudante(
                        user=user,
                        nome=nome,
                        email_institucional=email_institucional,
                        curso=curso,
                        periodo=periodo,
                        matricula=matricula
                    )
                    estudante.save()

                    return redirect('tela_estudante')
            except IntegrityError:
                form.add_error(None, "Erro ao criar o usuário. Por favor, tente novamente.")
    else:
        form = EstudanteRegistrationForm()

    return render(request, 'cadastrar_estudante.html', {'form': form})

# Function to register a professor
def cadastrar_professor(request):
    if request.method == 'POST':
        form = ProfessorRegistrationForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email_institucional = form.cleaned_data['email_institucional']
            senha = form.cleaned_data['senha']

            try:
                if User.objects.filter(email=email_institucional).exists():
                    form.add_error('email_institucional', 'Este email já está em uso.')
                else:
                    user = User.objects.create_user(
                        email=email_institucional,
                        password=senha
                    )

                    professor = Professor(
                        user=user,
                        nome=nome,
                        email_institucional=email_institucional
                    )
                    professor.save()

                    return redirect('home')
            except IntegrityError:
                form.add_error(None, "Erro ao criar o usuário. Por favor, tente novamente.")

    else:
        form = ProfessorRegistrationForm()

    return render(request, 'cadastrar_professor.html', {'form': form})

# Function to show student screen
def tela_estudante(request):
    return render(request, 'tela_estudante.html')

# Function to show professor screen
def tela_professor(request):
    return render(request, 'tela_professor.html')

# Login function
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        user = authenticate(request, email=email, password=senha)

        if user is not None:
            login(request, user)
            if hasattr(user, 'estudante'):
                return redirect('tela_estudante')
            elif hasattr(user, 'professor'):
                return redirect('tela_professor')
        else:
            messages.error(request, "Credenciais inválidas.")

    return render(request, 'form.html')  # Retorna a página com o formulário
