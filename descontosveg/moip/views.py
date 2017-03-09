from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from moip import MoIP
from descontosveg.book.models import Book
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json

def moipSend(request, id_book):
    book_selecionado = Book.objects.get(id=id_book)
    value = str(book_selecionado.value)
    razao = book_selecionado.name
    moip = MoIP(razao=razao,valor=value)
    moip.set_credenciais(token="IZXOTSU5G1ZXWZQRO4ZCDOOXGDWPBRTE",key="3T366IZHB8F7YZ22PMCJW5UXZNCDAXU7JVYH8IZY") 
    moip.envia()
    resposta = moip.get_resposta()
    return HttpResponseRedirect("https://desenvolvedor.moip.com.br/sandbox/Instrucao.do?token="+str(resposta['token']))


def formMoip(request):
	return render(request, 'teste_form.html')

@api_view(['POST'])
def moipResponse(request):
    if request.method == "POST":
        print request.data
        data = request.data
        arquivo = open('retorno_moip.txt', 'w')
        arquivo.write(str(data))
        arquivo.close()
        return HttpResponse()
    else:
        return HttpResponse()