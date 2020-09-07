from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('home', views.home, name='home'),
	path('home2', views.home2, name='home2'),
	path('login', views.login, name='login'),
	path('cadastro', views.cadastro, name='cadastro'),
	path('cadastro_empresas', views.cadastro_empresas, name='cadastro_empresas'),
	path('cadastro_preenchido', views.cadastro_preenchido, name='cadastro_preenchido'),
	path('candidaturas', views.candidaturas, name='candidaturas'),
	path('chatbot', views.chatbot, name='chatbot'),
	path('chat', views.chat, name='chat'),
	path('dashboard_empresas', views.dashboard_empresas, name='dashboard_empresas'),
	path('premium', views.premium, name='premium'),
	path('resultado_de_competencias', views.resultado_de_competencias, name='resultado_de_competencias'),
	path('tab_bar_ativa', views.tab_bar_ativa, name='tab_bar_ativa'),
	path('vagas', views.vagas, name='vagas'),
	path('vagas_inscricao_realizada', views.vagas_inscricao_realizada, name='vagas_inscricao_realizada'),

]
