from django.shortcuts import render
from django.http import HttpResponse
from models import Colecao
from django.template import Context, loader

def index(request):
    lista = Colecao.objects.all() #busca as colecoes
    t = loader.get_template('index.html') #indica o template
    c = Context ({'lista': lista}) #cria uma variável “lista” para o template
    return HttpResponse(t.render(c)) #renderiza o template


# Create your views here.
