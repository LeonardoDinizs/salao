from django.shortcuts import render
from .forms import AgendamentoForm

# Create your views here.
def agendamento(request):
   form = AgendamentoForm()
   return render(request, 'agendar/agendamento.html', {
      'form' : form,
   })