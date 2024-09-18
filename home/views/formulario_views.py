# flake8: noqa
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from home.forms import ContactForm


def enviar_formulario(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)  # Incluímos request.FILES para lidar com o arquivo
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            mensagem = form.cleaned_data['mensagem']
            arquivo = request.FILES.get('arquivo')  # Captura o arquivo se foi enviado

            # Enviar e-mail
            assunto = f"Mensagem de {nome}"
            corpo_email = f"Nome: {nome}\nEmail: {email}\n\nMensagem:\n{mensagem}"

            # Criar o objeto de e-mail
            email_mensagem = EmailMessage(
                assunto,
                corpo_email,
                'andersonpruzak.jobs@gmail.com',  # Seu e-mail de origem
                ['andersonpruzak.jobs@gmail.com'],  # E-mail de destino
            )

            # Verifica se há arquivo e anexa ao e-mail
            if arquivo:
                email_mensagem.attach(arquivo.name, arquivo.read(), arquivo.content_type)

            # Enviar o e-mail
            email_mensagem.send()

            # Redirecionar para a página de sucesso
            return redirect('/sucesso')
    else:
        form = ContactForm()

    return render(request, 'home/formulario.html', {'form': form})


def sucesso(request):
    return render(request, 'home/sucesso.html')