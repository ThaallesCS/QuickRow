from django.shortcuts import render
from django.conf import settings


def index(request):
    return render(request, 'QuickRow/aluno/index.html', {})


def gera_senha(request):
    return render(request, 'QuickRow/aluno/gerasenha.html', {})


def fila(request):
    return render(request, 'QuickRow/aluno/fila.html', {})


def atendente_index(request):
    return render(request, 'QuickRow/atendente/indexAtend.html', {})


def tipo_login(request):
    return render(request, 'QuickRow/tipoLogin.html', {})


def login_atendente(request):
    return render(request, 'QuickRow/atendente/loginAtend.html', {})


def login_gerente(request):
    return render(request, 'QuickRow/gerente/loginGeren.html', {})


def index_gerente(request):
    return render(request, 'QuickRow/gerente/index.html', {})


def controle(request):
    return render(request, 'QuickRow/gerente/designacao.html', {})
