from django.urls import path
from agendar import views

urlpatterns = [
    path('agendamento/', views.agendamento, name='agendamento.html'),
    path('confirmacao/<int:id>/', views.confirmacao, name='confirmacao.html'),
]