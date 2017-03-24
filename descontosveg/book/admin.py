# coding: utf-8
from django.contrib import admin
from descontosveg.book.models import Book, Sale, Partner
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from random import randint
from django.core.mail import send_mail, BadHeaderError






# Register your models here.




class BookAdmin(admin.ModelAdmin):

    
    list_display = ('name','description','status','value',)
    list_editable = ('value','status', )
    search_fields = ('name', )

    
    fields = ()
    
    
    
admin.site.register(Book, BookAdmin)





class SaleAdmin(admin.ModelAdmin):

    
    list_display = ('name','description','status',)
    list_editable = ()
    list_editable = ()
    search_fields = ()
    fields = ()
    
    
    
admin.site.register(Sale, SaleAdmin)


class PartnerAdmin(admin.ModelAdmin):



    
    list_display = ('name','user','email','site','address','phone')
    list_editable = ()
    list_editable = ()
    search_fields = ('name','user','email','site','address','phone')
    fields = ('name','user','email','site', 'address','phone')

    
    
    
admin.site.register(Partner, PartnerAdmin)

def reset_password(modeladmin, request, queryset):
    for usuario in queryset:
        senha = str(randint(100000,999999))
        usuario.set_password(senha)
        usuario.save()
        #envia email para o descontos veg e para o usuario informando a nova senha
        envia_email(usuario, senha)

reset_password.short_description = "Resetar senha"

class MyUserAdmin(UserAdmin):
    actions = [reset_password]


admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)



def envia_email(usuario, nova_senha):
    message = "Você solicitou uma nova senha no vegdescontos. \n Sua nova senha é: "+ nova_senha
    try:
        send_mail("VegDescontos" ,message , 'descontosveg@gmail.com', ['descontosveg@gmail.com',usuario.email])

        print "sucesso"
    except BadHeaderError:
        print "falha"

