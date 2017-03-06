from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from moip import MoIP

def moipSend(request, valor):
    moip = MoIP(razao="Razao",valor=valor)
    moip.set_credenciais(token="IZXOTSU5G1ZXWZQRO4ZCDOOXGDWPBRTE",key="3T366IZHB8F7YZ22PMCJW5UXZNCDAXU7JVYH8IZY") 
    moip.envia()
    resposta = moip.get_resposta()
    return HttpResponseRedirect("https://desenvolvedor.moip.com.br/sandbox/Instrucao.do?token="+str(resposta['token']))


def formMoip(request):
	return render(request, 'teste_form.html')