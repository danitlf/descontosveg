# coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from moip import MoIP
from descontosveg.book.models import Book, Sale
from descontosveg.moip.models import Purchase, User_Sales
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.contrib.auth.decorators import login_required
import sys    # sys.setdefaultencoding is cancelled by site.py
reload(sys)    # to re-enable sys.setdefaultencoding()
sys.setdefaultencoding('utf-8')



@login_required(login_url='/login/')
def moipSend(request, id_book):
    book_selecionado = Book.objects.get(id=id_book)
    value = str(book_selecionado.value)
    razao = str(book_selecionado.name)

    #creating obj of Purchase
    purchase = Purchase(state="0", value=book_selecionado.value, book=book_selecionado, user=request.user)
    purchase.save()


    moip = MoIP(razao=razao,valor=value)
    moip.set_credenciais(token="IZXOTSU5G1ZXWZQRO4ZCDOOXGDWPBRTE",key="3T366IZHB8F7YZ22PMCJW5UXZNCDAXU7JVYH8IZY") 
    moip.set_id_proprio(str(purchase.id))
    moip.envia()
    resposta = moip.get_resposta()
    print resposta
    return HttpResponseRedirect("https://desenvolvedor.moip.com.br/sandbox/Instrucao.do?token="+str(resposta['token']))


def formMoip(request):
	return render(request, 'teste_form.html')

@api_view(['POST'])
@csrf_exempt
def moipResponse(request):
    if request.method == "POST":
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
    compra = Purchase.objects.get(id=dados["id_transacao"])
    compra.forma_pagamento = dados["forma_pagamento"]
    compra.tipo_pagamento = dados["tipo_pagamento"]
    compra.state = dados["status_pagamento"]
    compra.date = datetime.strptime(dados["status_data"], "%Y/%m/%d-%H:%M:%S")
    compra.id_moip = dados["cod_moip"]
    compra.save()
    obj_da_compra = Purchase.objects.get(id=dados["id_transacao"])
    if dados["status_pagamento"] == "4":

        #insere todas as ofertas que existiam no book comprado
        insere_ofertas_do_usuario(obj_da_compra)



def insere_ofertas_do_usuario(compra):
    sales_do_book = Sale.objects.filter(books=compra.book)
    for sale in sales_do_book:

        #gera o id da oferta daquele usuario
        id_user_sale = str(sale.id) + str(compra.id_moip)
        
        #salva na tabela as ofertas do usuario
        user_sale = User_Sales(sale=sale, user=compra.user, state="1", purchase=compra, id_user_sale=id_user_sale)
        user_sale.save()






