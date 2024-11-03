from django.urls import path
from agendar import views

urlpatterns = [
    path('agendamento/', views.agendamento, name='agendamento.html'),

]