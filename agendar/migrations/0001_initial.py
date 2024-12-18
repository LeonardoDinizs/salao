# Generated by Django 5.1.1 on 2024-10-25 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('celular', models.CharField(max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('servicos', models.CharField(choices=[('corte_masculino', 'Corte Masculino'), ('corte_feminino', 'Corte Feminino'), ('corte_infantil', 'Corte Infantil'), ('coloracao', 'Coloração'), ('selagem', 'Selagem'), ('hidratacao', 'Hidratação'), ('progressiva', 'Progressiva Orgânica Sem Formol'), ('outros', 'Outros')], max_length=50)),
                ('data_desejada', models.DateField()),
                ('horario_desejado', models.TimeField()),
                ('mensagem', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
