from django.contrib import admin
from descontosveg.moip.models import User_Sales, Purchase





class User_SalesAdmin(admin.ModelAdmin):

	
    
    list_display = ('sale','user','purchase','state',)
    list_editable = ('state', )
    search_fields = ('sale','user','state', )
    readonly_fields = ('sale','user','purchase',)
     
admin.site.register(User_Sales, User_SalesAdmin)

# Register your models here.

#admin.site.register(User_Sales)
admin.site.register(Purchase)

