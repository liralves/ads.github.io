
from django.contrib import admin
from django.urls import path
from appweb import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('form/', views.form, name='form'),
    path('tipo_cadastro/', views.tipo_cadastro, name='tipo_cadastro'),
    path('cadastrar_estudante/', views.cadastrar_estudante, name='cadastrar_estudante'),
    path('cadastrar_professor/', views.cadastrar_professor, name='cadastrar_professor'),
    path('tela_estudante/', views.tela_estudante, name='tela_estudante'),
    path('tela_professor/', views.tela_professor, name='tela_professor'),
    path('login/', views.login_view, name='login')
]
