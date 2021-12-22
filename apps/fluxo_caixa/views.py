from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def cadastrar_despesa(request):
    return render(request, 'cadastrar_despesa.html')