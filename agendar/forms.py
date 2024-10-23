from django import forms

class AgendamentoForm(forms.Form):
    nome = forms.CharField(
        label="Nome:", 
        max_length=100, 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu nome completo'})
    )
    
    celular = forms.CharField(
        label="Celular:", 
        max_length=15, 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu celular para contato'})
    )
    
    email = forms.EmailField(
        label="Email: (opcional)", 
        required=False, 
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu e-mail (opcional)'})
    )
    
    SERVICOS_CHOICES = [
        ('corte_masculino', 'Corte Masculino'),
        ('corte_feminino', 'Corte Feminino'),
        ('corte_infantil', 'Corte Infantil'),
        ('coloracao', 'Coloração'),
        ('selagem', 'Selagem'),
        ('hidratacao', 'Hidratação'),
        ('progressiva', 'Progressiva Orgânica Sem Formol'),
        ('outros', 'Outros')
    ]
    
    servicos = forms.MultipleChoiceField(
    label="Serviços Desejados:", 
    choices=SERVICOS_CHOICES, 
    required=True, 
    widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    )
    
    data_desejada = forms.DateField(
        label="Data Desejada:", 
        required=True, 
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    
    horario_desejado = forms.TimeField(
        label="Horário Desejado:", 
        required=True, 
        widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'})
    )
    
    mensagem = forms.CharField(
        label="Mensagem: (opcional)", 
        required=False, 
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Escreva uma mensagem ou observação'})
    )
