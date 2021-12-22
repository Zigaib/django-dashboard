# Generated by Django 3.2.6 on 2021-12-20 00:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fluxo_caixa', '0012_alter_lancamento_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_Operacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('E', 'Entrada'), ('S', 'Saída')], default='E', max_length=1)),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='lancamento',
            name='plano_conta',
        ),
        migrations.RemoveField(
            model_name='lancamento',
            name='tipo',
        ),
        migrations.DeleteModel(
            name='Plano_Conta',
        ),
        migrations.AddField(
            model_name='lancamento',
            name='tipo_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fluxo_caixa.tipo_operacao'),
            preserve_default=False,
        ),
    ]
