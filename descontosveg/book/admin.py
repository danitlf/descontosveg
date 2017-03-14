from django.contrib import admin
from descontosveg.book.models import Book, Sale, Partner
from django.contrib.auth.models import User



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

    
    list_display = ('name','cnpj','email','address','phone')
    list_editable = ()
    list_editable = ()
    search_fields = ('name','cnpj','email','address','phone')
    fields = ('name','cnpj','email','address','phone','password')

    
    
    
admin.site.register(Partner, PartnerAdmin)









