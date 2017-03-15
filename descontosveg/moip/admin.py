from django.contrib import admin
from descontosveg.moip.models import User_Sales, Purchase
from descontosveg.book.models import Partner, Sale
from django.contrib.auth.models import User






class User_SalesAdmin(admin.ModelAdmin):

	#filtra as ofertas para o parceiro 
    def get_queryset(self, request): 

		qs = super(User_SalesAdmin, self).get_queryset(request) 

		if not request.user.is_superuser: 
			partner = Partner.objects.get(user=request.user)
			sales = Sale.objects.filter(partner=partner)


			return qs.filter(sale=sales) 
		else: 
			
			return qs 
    
    list_display = ('sale','user','purchase','state',)
    list_editable = ('state', )
    search_fields = ('sale','user','state', )
    readonly_fields = ('sale','user','purchase',)
     
admin.site.register(User_Sales, User_SalesAdmin)

# Register your models here.

#admin.site.register(User_Sales)
admin.site.register(Purchase)

