from __future__ import unicode_literals
from django.db import models

# Create your models here.

from django.utils.translation import ugettext_lazy as _

class Purchase(models.Model):
    
    user = models.ForeignKey('book.Person', null=True, blank=True)
    name = models.CharField(_('nome'),max_length=100)
    tipo_pagamento = models.CharField(_('tipo_pagamento'),max_length=100, null=True, blank=True)
    forma_pagamento = models.CharField(_('forma_pagamento'),max_length=100, null=True, blank=True)
    state = models.CharField(_('status'),max_length=200)
    value = models.CharField(_('value'),max_length=200, null=True, blank=True)
    token = models.CharField(_('token'),max_length=300)
    id_moip =  models.CharField(_('id_moip'),max_length=200, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    
class User_Sales(models.Model):
	sale = models.ForeignKey('book.Sale')
	state = models.CharField(_('status'),max_length=200)
	user = models.ForeignKey('book.Person')
	purchase = models.ForeignKey('Purchase')