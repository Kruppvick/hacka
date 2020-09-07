from django.shortcuts import render

def index(request):
    return render (request, 'index.html');

def home(request):
    return render(request, 'home.html');

def home2(request):
    return render(request, 'home2.html');

def login(request):
    return render(request, 'login.html');

def cadastro(request):
    return render(request, 'cadastro.html');

def cadastro_preenchido(request):
    return render(request, 'cadastro-preenchido.html');

def cadastro_empresas(request):
    return render(request, 'cadastro-empresas.html');

def candidaturas(request):
    return render(request, 'candidaturas.html');

def chatbot(request):
    return render(request, 'chatbot.html');

def chat(request):
    return render(request, 'chat.html');

def premium(request):
    return render(request, 'premium.html');

def resultado_de_competencias(request):
    return render(request, 'resultado-de-competencias.html');

def tab_bar_ativa(request):
    return render(request, 'tab-bar-ativa.html');

def vagas(request):
    return render(request, 'vagas.html');

def vagas_inscricao_realizada(request):
    return render(request, 'vagas-inscricao-realizada.html');

def dashboard_empresas(request):
    return render(request, 'dashboard-empresas.html');
