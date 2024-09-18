from django.urls import path
from home import views

app_name = 'home'

urlpatterns = [
    path('',
         views.index,
         name='index'
         ),
    path('enviar/',
         views.enviar_formulario,
         name='enviar_formulario'
         ),
    path('sucesso/',
         views.sucesso,
         name='sucesso'
         ),
    path('projetos/',
         views.projetos,
         name='projetos'
         ),
    path('obras/',
         views.obras,
         name='obras'
         ),
    path('materiais/',
         views.materiais,
         name='materiais'
         ),
    path('servicos/',
         views.servicos,
         name='servicos'
         ),
    path(
        'analise-qualidade-energia/',
        views.analise,
        name='analise_qualidade_energia'
        ),
    path('acessoria_consultoria/',
         views.acessoria_consultoria,
         name='acessoria_consultoria'
         ),
    path('laudos_inspecoes/',
         views.laudos_inspecoes,
         name='laudos_inspecoes'
         ),
]
