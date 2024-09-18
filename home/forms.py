from django import forms
from django.core.exceptions import ValidationError


class ContactForm(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.EmailField()
    mensagem = forms.CharField(widget=forms.Textarea)
    arquivo = forms.FileField(required=False)

    def clean_arquivo(self):
        arquivo = self.cleaned_data.get('arquivo', False)

        if arquivo:
            # Verifica se o arquivo é um PDF
            if arquivo.content_type != 'application/pdf':
                raise ValidationError(
                    "Por favor, envie um arquivo no formato PDF.")

            # Verifica o tamanho do arquivo (opcional, aqui limitando a 20MB)
            if arquivo.size > 20 * 1024 * 1024:
                raise ValidationError(
                    "O arquivo não pode ser maior que 20MB.")

        return arquivo
