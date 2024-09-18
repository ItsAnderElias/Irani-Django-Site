from django.shortcuts import render


def projetos(request):
    print('Projetos Acessed')
    context = {
        'title': 'Projetos'
    }
    return render(
        request,
        'home/projetos.html',
        context
    )


def obras(request):
    print('Obras Acessed')
    context = {
        'title': 'Obras'
    }
    return render(
        request,
        'home/obras.html',
        context
    )


def materiais(request):
    print('Materiais Acessed')
    context = {
        'title': 'Materiais Elétricos'
    }
    return render(
        request,
        'home/materiais.html',
        context
    )


def servicos(request):
    print('Servicos Acessed')
    context = {
        'title': 'Serviços'
    }
    return render(
        request,
        'home/servicos.html',
        context
    )


def analise(request):
    print('Analise Acessed')
    context = {
        'title': 'Análise de Qualidade de Energia'
    }
    return render(
        request,
        'home/analise.html',
        context
    )


def acessoria_consultoria(request):
    print('acessoria_consultoria Acessed')
    context = {
        'title': 'Acessoria e Consultoria'
    }
    return render(
        request,
        'home/acessoria_consultoria.html',
        context
    )


def laudos_inspecoes(request):
    print('laudos_inspecoes Acessed')
    context = {
        'title': 'Laudos e Inspeções'
    }
    return render(
        request,
        'home/laudos_inspecoes.html',
        context
    )
