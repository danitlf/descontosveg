from django.shortcuts import render
from django.http import HttpResponse
from moip import MoIP

def moipSend(request):
    moip = MoIP(razao="Razao",valor="150.00")
    moip.set_credenciais(token="IZXOTSU5G1ZXWZQRO4ZCDOOXGDWPBRTE",key="3T366IZHB8F7YZ22PMCJW5UXZNCDAXU7JVYH8IZY") 
    moip.envia()
    resposta = moip.get_resposta()
    return HttpResponse("Token retornado: "+resposta['token'])