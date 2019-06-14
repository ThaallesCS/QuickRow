"""QuickRow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from QuickRow import views
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('gerasenha/', views.gera_senha, name='gerasenha'),
    path('gerasenha/fila/', views.fila, name='fila'),
    path('tipo_login/', views.tipo_login, name='tipo_login'),
    path('atendente/', views.atendente_index, name='indexAtendente'),
    path('tipo_login/login_atendente/', views.login_atendente, name='login_atendente'),
    path('tipo_login/login_gerente/', views.login_gerente, name= 'login_gerente'),
    path('inicio_gerente/', views.index_gerente, name='inicio_gerente'),
    path('controle', views.controle, name='controle'),


    #path('', include('site.urls')),

]
import os
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
STATICFILES_DIRS = (
  os.path.join(SITE_ROOT, 'static/'),
)
