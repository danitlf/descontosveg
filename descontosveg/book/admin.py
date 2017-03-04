from django.contrib import admin

from descontosveg.book.models import Book, Sale

# Register your models here.




class BookAdmin(admin.ModelAdmin):

    
    list_display = ('name','description','status',)
    list_editable = ()
    search_fields = ()
    fields = ()
    
    
    
admin.site.register(Book, BookAdmin)





class SaleAdmin(admin.ModelAdmin):

    
    list_display = ('name','description','status',)
    list_editable = ()
    list_editable = ()
    search_fields = ()
    fields = ()
    
    
    
admin.site.register(Sale, SaleAdmin)