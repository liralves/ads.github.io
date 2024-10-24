from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O email deve ser fornecido.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class Estudante(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Relaciona o estudante ao usuário
    nome = models.CharField(max_length=100)
    email_institucional = models.EmailField()
    curso = models.CharField(max_length=100)
    periodo = models.CharField(max_length=10)
    matricula = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Relaciona o professor ao usuário
    nome = models.CharField(max_length=100)
    email_institucional = models.EmailField()
    departamento = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
