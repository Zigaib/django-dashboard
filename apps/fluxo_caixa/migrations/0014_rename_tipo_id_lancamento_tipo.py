# Generated by Django 3.2.6 on 2021-12-21 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fluxo_caixa', '0013_auto_20211220_0047'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lancamento',
            old_name='tipo_id',
            new_name='tipo',
        ),
    ]
