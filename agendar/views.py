# views.py
from django.shortcuts import render, redirect
from .forms import AgendamentoForm
from .models import Agendamento

def agendamento(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            agendamento = Agendamento(
                nome=form.cleaned_data['nome'],
                celular=form.cleaned_data['celular'],
                email=form.cleaned_data['email'],
                servicos=', '.join(form.cleaned_data['servicos']),
                data_desejada=form.cleaned_data['data_desejada'],
                horario_desejado=form.cleaned_data['horario_desejado'],
                mensagem=form.cleaned_data['mensagem'],
            )
            agendamento.save()
            # Redireciona para a página de confirmação após salvar
            return redirect('confirmacao.html', id=agendamento.id)  # Redireciona para a confirmação
    else:
        form = AgendamentoForm()
    
    return render(request, 'agendar/agendamento.html', {'form': form})

def confirmacao(request, id):
    agendamento = Agendamento.objects.get(id=id)  # Obtém o agendamento pelo ID
    return render(request, 'agendar/confirmacao.html', {'agendamento': agendamento})
