# Generated by Django 3.2.6 on 2021-11-01 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fluxo_caixa', '0004_rename_lancameto_lancamento'),
    ]

    operations = [
        migrations.AddField(
            model_name='plano_conta',
            name='tipo',
            field=models.CharField(choices=[('A', 'Analitica'), ('S', 'Sintetica'), ('I', 'Inteira')], default='I', max_length=1),
            preserve_default=False,
        ),
    ]
