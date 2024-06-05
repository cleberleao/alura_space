from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    dados = {
        1: {
            'nome': 'Nebulosa de Carina',
            'legenda': 'webbtelescope.org / NASA / James Webb'
        },
        2: {
            'nome': 'Galaxia de Andrômeda',
            'legenda': 'NASA / ESA / J. Dalcanton'
        },
    }
    return render(request, 'galeria/index.html', {'cards': dados})

def imagem(request):
    return render(request, 'galeria/imagem.html')