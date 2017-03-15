from __future__ import unicode_literals
from django.db import models

# Create your models here.

from django.utils.translation import ugettext_lazy as _



STATUS_CHOICES = (
    ('1', 'Autorizado'),
    ('2', 'Iniciado'),
    ('3', 'Boleto Impresso'),
    ('4', 'Concluido'),
    ('5', 'Cancelado'),
    ('6', 'Em analise'),
    ('7', 'Estornado'),
    ('9', 'Reembolsado')

)


STATUS_CHOICES2 = (
    ('0', 'Utilizado'),
    ('1', 'Disponivel')
    

)

class Purchase(models.Model):
    
    user = models.CharField(_('CPF'), null=True, blank=True,max_length=11)
    book = models.ForeignKey('book.Book',  null=True, blank=True)
    tipo_pagamento = models.CharField(_('tipo_pagamento'),max_length=100, null=True, blank=True)
    forma_pagamento = models.CharField(_('forma_pagamento'),max_length=100, null=True, blank=True)
    state = models.CharField(_('status'),max_length=200,choices=STATUS_CHOICES)
    value = models.CharField(_('value'),max_length=200, null=True, blank=True)
    token = models.CharField(_('token'),max_length=300)
    id_moip =  models.CharField(_('id_moip'),max_length=200, null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return (str(self.pk))
    
class User_Sales(models.Model):
    sale = models.ForeignKey('book.Sale')
    state = models.CharField(_('status'),max_length=1, choices=STATUS_CHOICES2)
    user = models.CharField(_('CPF'), null=True, blank=True,max_length=11)
    purchase = models.ForeignKey('Purchase')
    id_user_sale = models.CharField(_('ID_OFERTA_USUARIO'), null=True, blank=True, max_length=501)

