from django.shortcuts import render
from django.conf import settings
from descontosveg.book.models import Book,Sale
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from descontosveg.book.forms import ContactForm

# Create your views here.


def home(request):

    #context = {'STATIC_URL': settings.STATIC_URL}
    
    book = Book.objects.all()
    sale = Sale.objects.all()
    form_class = ContactForm



    return render(request, 'index.html', {'form': form_class,'book':book,'sale':sale, 'STATIC_URL': settings.STATIC_URL})

def contact(request):
    form_class = ContactForm
    
    return render(request, 'contact.html', {
        'form': form_class,
    })


def send_email(request):
    subject = request.POST.get('contact_name')
    message = request.POST.get('content')
    from_email = request.POST.get('contact_email')
    message = message + "\n from: "+ str(from_email)
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['descontosveg@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponse('thanks')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')



