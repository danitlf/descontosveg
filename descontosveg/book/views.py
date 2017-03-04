from django.shortcuts import render
from django.conf import settings
from descontosveg.book.models import Book,Sale


# Create your views here.


def home(request):

    #context = {'STATIC_URL': settings.STATIC_URL}
    
    book = Book.objects.all()
    sale = Sale.objects.all()



    return render(request, 'index.html', {'book':book,'sale':sale, 'STATIC_URL': settings.STATIC_URL})



