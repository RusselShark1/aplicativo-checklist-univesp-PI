from django.urls import path
from . import views

urlpatterns = [
    path('', views.fazer_login, name='login'),
    path('sair/', views.deslogar, name='logout'),
    path('checklist/', views.cadastrar, name='cadastrar'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('senha/', views.mudar_senha, name='mudar_senha'),
]