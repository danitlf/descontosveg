from django.db import models
from django.utils.translation import ugettext_lazy as _







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

    books = models.ForeignKey('Book',verbose_name=_('Livro'))




    class Meta:
        verbose_name = _('Oferta')
        verbose_name_plural = _('Ofertas')

    def __unicode__(self):
        return (self.name)


class Partner(models.Model):

    name = models.CharField(_('Nome'),max_length=100)     
    cnpj = models.IntegerField(_('CNPJ'),max_length=20)  


class User(models.Model):

    partner = models.ForeignKey('Partner',verbose_name=_('CNPJ do Parceiro'))



	

