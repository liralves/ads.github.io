from django import forms
from .models import Estudante, Professor

# forms.py

class EstudanteRegistrationForm(forms.Form):
    nome = forms.CharField(max_length=100, label="Nome")
    email_institucional = forms.EmailField(label="Email Institucional")
    curso = forms.CharField(max_length=100, label="Curso")
    periodo = forms.CharField(max_length=10, label="Período")
    matricula = forms.CharField(max_length=20, label="Matrícula")
    senha = forms.CharField(widget=forms.PasswordInput(), label="Senha")

    class Meta:
        model = Estudante
        fields = ['nome', 'email_institucional', 'curso', 'periodo', 'matricula', 'senha']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class ProfessorRegistrationForm(forms.Form):
    nome = forms.CharField(max_length=100, label="Nome")
    email_institucional = forms.EmailField(label="Email Institucional")
    departamento = forms.CharField(max_length=100, label="Departamento")
    senha = forms.CharField(widget=forms.PasswordInput(), label="Senha")

    class Meta:
        model = Professor
        fields = ['nome', 'email_institucional', 'departamento', 'senha']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
