# Generated by Django 3.2.6 on 2021-11-01 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fluxo_caixa', '0009_auto_20211101_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plano_conta',
            name='tipo',
            field=models.CharField(choices=[('A', 'Analitica'), ('S', 'Sintetica'), ('P', 'Pai')], max_length=1),
        ),
    ]