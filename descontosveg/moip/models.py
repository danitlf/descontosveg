from __future__ import unicode_literals
from django.db import models
from descontosveg.book.models import Person

# Create your models here.

from django.utils.translation import ugettext_lazy as _

class Purchase(models.Model):
    
    user = models.ForeignKey(Person)
    name = models.CharField(_('nome'),max_length=100)
    state = models.CharField(_('status'),max_length=200)
    token = models.CharField(_('token'),max_length=300)

    

		