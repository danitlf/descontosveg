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
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    image = models.ImageField(_('Imagem:'),null=True, blank=True, upload_to= 'uploads')

    
    class Meta:
        abstract = True


class Book(Usual): 

    class Meta:
        verbose_name = _('Livro')
        verbose_name_plural = _('Livros')

    def __unicode__(self):
        return (self.name)


class Sale(Usual):

    image2 = models.ImageField(_('Imagem 2:'),null=True, blank=True, upload_to= 'uploads')
    image3 = models.ImageField(_('Imagem 3:'),null=True, blank=True, upload_to= 'uploads')
    validity = models.CharField(_('Validade'),max_length=100,null=True, blank=True)
    rules = models.TextField(_('Regras de uso'),max_length=100,blank=True)
    partner = models.ForeignKey('Partner')
    books = models.ForeignKey('Book',verbose_name=_('Livro'))



    class Meta:
        verbose_name = _('Oferta')
        verbose_name_plural = _('Ofertas')

    def __unicode__(self):
        return (self.name)


class Partner(models.Model):

    name = models.CharField(_('Nome'),max_length=110,null=True, blank=True) 
    address = models.CharField(_('Endereco'),max_length=100,null=True, blank=True)
    phone = models.CharField(_('Telefone'),max_length=100,null=True, blank=True)     
    email = models.CharField(_('Email'),max_length=100,null=True, blank=True)
    site = models.CharField(_('Site'),max_length=100,null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True)


    class Meta:
        verbose_name = _('Parceiro')
        verbose_name_plural = _('Parceiros')


    def __unicode__(self):
        return (self.name) 







	

