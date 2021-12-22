from django import db
from django.contrib import admin
from django.db.models import Q
from .models import *

@admin.register(Lancamento)
class LancamentoAdmin(admin.ModelAdmin):
    list_display = ('data', 'no_documento', 'descricao', 'valor', 'tipo_id', 'user')
    list_filter = ('data', 'no_documento', 'descricao', 'valor', 'tipo_id', 'user')
    search_fields = ('data', 'no_documento', 'descricao', 'valor', 'tipo_id', 'user')

@admin.register(Tipo_Operacao)
class Tipo_OperacaoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'descricao')
    list_filter = ('tipo', 'descricao')
    search_fields = ('tipo', 'descricao')
