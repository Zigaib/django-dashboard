from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from apps.fluxo_caixa.models import Lancamento, Tipo_Operacao
from django.db.models import Sum

from datetime import timedelta, date


@login_required(login_url="/login/")
def index(request):

    result = Tipo_Operacao.objects.all()

    lancamento = Lancamento.objects.all()
    status = {"Entrada": lancamento.filter(tipo__tipo="E").count(), 
            "Saida": lancamento.filter(tipo__tipo="S").count(),
            "Total": lancamento.count()}

    valores = Lancamento.objects.filter(tipo__tipo="E", data__gte=date.today()-timedelta(days=7)).aggregate(total=Sum('valor'))

    
    context = {'segment': 'index', 'result': result, 'status': status, 'valores': valores}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def index_v2(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index_ori.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
