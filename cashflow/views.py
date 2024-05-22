from django.shortcuts import render, redirect
from .forms import ProdutoForm, TransacaoForm
from .models import FluxoCaixa, Produto, Transacao
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.utils.timezone import now
from datetime import timedelta


@login_required
def adicionar_produto(request):
    if request.method == "Post":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProdutoForm()
    return render(request, 'cashflow/adicionar_produto.html', {'form': form})

@login_required
def adicionar_transacao(request):
    if request.method == "Post":
        form = TransacaoForm(request.POST)
        if form.is_valid():
            transacao = form.save()
            FluxoCaixa.objects.create(usuario=request.user, transacao=transacao)
            return redirect('home')
    else:
        form = TransacaoForm()
    return render(request, 'cashflow/adicionar_transacao.html', {'form': form})

@login_required
def relatorios(request):
    hoje = now().date()
    semana_passada = hoje - timedelta(days=7)
    mes_passado = hoje - timedelta(days=30)

    relatorio_diario = Transacao.objects.filter(data_hora__date=hoje).aggregate(total=Sum('valor'))
    relatorio_semanal = Transacao.objects.filter(data_hora__date__gte=semana_passada).aggregate(total=Sum('valor'))
    relatorio_mensal = Transacao.objects.filter(data_hora__date__gte=mes_passado).aggregate(total=Sum('valor'))

    context = {
        'relatorio_diario': relatorio_diario,
        'relatorio_semanal': relatorio_semanal,
        'relatorio_mensal': relatorio_mensal,
    }
    return render(request, 'cashflow/relatorios.html', context)

@login_required
def home(request):
    return render(request, 'cashflow/home.html')
