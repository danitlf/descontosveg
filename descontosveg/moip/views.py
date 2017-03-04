from django.shortcuts import render
from django.http import HttpResponse
from moip import MoIP

def moipSend(request):
    moip = MoIP(razao="Razao",valor="150.00")
    moip.set_credenciais(token="seu_token",key="sua_key") 
    moip.envia()
    resposta = moip.get_resposta()
    return HttpResponse("Token retornado: "+resposta['token'])