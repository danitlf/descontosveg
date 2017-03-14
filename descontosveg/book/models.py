from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User






STATUS_CHOICES = (
    ('d', 'Despublicado'),
    ('p', 'Publicado'),    
)







class Usual(models.Model):
    
    name = models.CharField(_('titulo'),max_length=100)
    description = models.TextField(_('descricao'),max_length=100,blank=True)
    value = models.DecimalField(null=True, blank=True, default=None,decimal_places=2,max_digits=5)
    image = models.ImageField(_('Imagem:'),null=True, blank=True, upload_to= 'uploads')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    
    class Meta:
        abstract = True





class Book(Usual): 

    




    class Meta:
        verbose_name = _('Livro')
        verbose_name_plural = _('Livros')

    def __unicode__(self):
        return (self.name)





class Sale(Usual):

    partner = models.ForeignKey('Partner')
    books = models.ForeignKey('Book',verbose_name=_('Livro'))




    class Meta:
        verbose_name = _('Oferta')
        verbose_name_plural = _('Ofertas')

    def __unicode__(self):
        return (self.name)


class Partner(models.Model):

    name = models.CharField(_('Nome'),max_length=100,null=True, blank=True) 
    email = models.CharField(_('Email'),max_length=100,null=True, blank=True)
    address = models.CharField(_('Endereco'),max_length=100,null=True, blank=True)
    phone = models.CharField(_('Telefone'),max_length=100,null=True, blank=True)     
    cnpj = models.BigIntegerField(_('CNPJ')) 
    password = models.CharField(_('Crie uma senha'),max_length=50,null=True, blank=True)


    class Meta:
        verbose_name = _('Parceiro')
        verbose_name_plural = _('Parceiros')


    def __unicode__(self):
        return (self.name) 






	

