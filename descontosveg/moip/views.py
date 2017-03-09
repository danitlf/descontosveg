from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from moip import MoIP
from descontosveg.book.models import Book
from descontosveg.moip.models import Purchase, User_Sales
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime


def moipSend(request, id_book):
    book_selecionado = Book.objects.get(id=id_book)
    value = str(book_selecionado.value)
    razao = book_selecionado.name

    #creating obj of Purchase
    purchase = Purchase(name=book_selecionado.name, state="0", value=book_selecionado.value)
    purchase.save()


    moip = MoIP(razao=razao,valor=value)
    moip.set_credenciais(token="IZXOTSU5G1ZXWZQRO4ZCDOOXGDWPBRTE",key="3T366IZHB8F7YZ22PMCJW5UXZNCDAXU7JVYH8IZY") 
    moip.set_id_proprio(str(purchase.id))
    moip.envia()
    resposta = moip.get_resposta()

    return HttpResponseRedirect("https://desenvolvedor.moip.com.br/sandbox/Instrucao.do?token="+str(resposta['token']))


def formMoip(request):
	return render(request, 'teste_form.html')

@api_view(['POST'])
@csrf_exempt
def moipResponse(request):
    if request.method == "POST":
        print request.data
        data = request.data

        atualiza_compra(data)

        
        # teste de recebimento de dados do MoIP
        # arquivo = open('retorno_moip.txt', 'w')
        # arquivo.write(str(data))
        # arquivo.close()


        return HttpResponse()
    else:
        return HttpResponse()


#com o retorno do moip nos atualizamos o registro
def atualiza_compra(dados):
    compra = Purchase.objects.get(id=dados["id_transacao"][0])
    compra.forma_pagamento = dados["forma_pagamento"][0]
    compra.tipo_pagamento = dados["tipo_pagamento"][0]
    compra.state = dados["status_pagamento"][0]
    compra.date = datetime.strptime(dados["status_data"][0], "%Y/%m/%d-%H:%M:%S")
    compra.id_moip = dados["status_data"][0]
    compra.save()
