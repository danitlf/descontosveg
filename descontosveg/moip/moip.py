#*-* encoding:utf-8 *-*
from lxml import etree
import os


class MoIP:
    """
    Classe para montar o XML de instrucoes
    """

    #url do sandbox
    url = "https://desenvolvedor.moip.com.br/sandbox/ws/alpha/EnviarInstrucao/Unica"


    def __init__(self,razao,valor):
        """
        Inicializa o objeto MoIP com os valores obrigatorios
        """
        enviar_instrucao = etree.Element("EnviarInstrucao")
        instrucao_unica = etree.SubElement(enviar_instrucao,"InstrucaoUnica")
        _razao = etree.SubElement(instrucao_unica,"Razao")
        _razao.text = razao
        valores = etree.SubElement(instrucao_unica,"Valores")
        _valor = etree.SubElement(valores,"Valor",moeda="BRL")
        _valor.text = valor

        self.enviar_instrucao = enviar_instrucao 
        

    def get_xml(self):
        """
        Retorna o XML gerado até agora
        """
        return etree.tostring(self.enviar_instrucao)

    def set_id_proprio(self,id):
        instrucao_unica = self.enviar_instrucao[0]
        id_proprio = etree.SubElement(instrucao_unica,"IdProprio")
        id_proprio.text = id
        return self

    def set_data_vencimento(self,data):
        instrucao_unica = self.enviar_instrucao[0]
        data_vencimento = etree.SubElement(instrucao_unica,"DataVencimento")
        data_vencimento.text = data
        return self

    def set_recebedor(self,login_moip,email,apelido):
        instrucao_unica = self.enviar_instrucao[0]
        recebedor = etree.SubElement(instrucao_unica,"Recebedor")
        _login_moip = etree.SubElement(recebedor,"LoginMoip")
        _login_moip.text = login_moip
        _email = etree.SubElement(recebedor,"Email")
        _email.text = email
        _apelido = etree.SubElement(recebedor,"Apelido")
        _apelido.text = apelido

        return self
    
    def set_ambiente(self,ambiente):
        if ambiente=="sandbox":
            self.url = "https://desenvolvedor.moip.com.br/sandbox/ws/alpha/EnviarInstrucao/Unica"
        elif ambiente=="producao":
            self.url = "https://www.moip.com.br/ws/alpha/EnviarInstrucao/Unica"

        return self

    def envia(self):
        self.command = 'curl -silent -u %s:%s -X POST -d \'%s\' %s' % (self.token,self.key,self.get_xml(),self.url)
        ret = os.popen(self.command)
        self.retorno = ret.readlines()[-1]
        return self

    def set_credenciais(self,token,key):
        self.token = token
        self.key = key

    def get_resposta(self):
        resposta = etree.XML(self.retorno)
        return {'sucesso':resposta[0][1].text,'token':resposta[0][2].text}