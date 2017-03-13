from django.shortcuts import render
from django.conf import settings
from descontosveg.book.models import Book,Sale

from descontosveg.moip.models import User_Sales

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from descontosveg.book.forms import ContactForm, UserForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.


def home(request):

    #context = {'STATIC_URL': settings.STATIC_URL}
    
    book = Book.objects.all()
    sale = Sale.objects.all()
    form_class = ContactForm



    return render(request, 'index.html', {'form': form_class,'book':book,'sale':sale, 'STATIC_URL': settings.STATIC_URL})


def cadastro(request):

    if request.method == "POST":
        formUser = UserForm(request.POST)
        if formUser.is_valid():
            new_user = User.objects.create_user(**formUser.cleaned_data)
            #login(new_user)
            # redirect, or however you want to get to the main view
            return HttpResponseRedirect('/')
    else:
        formUser = UserForm() 

    return render(request, 'cadastro.html',{'formUser': formUser,'STATIC_URL': settings.STATIC_URL})    




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


@login_required
def pedidos(request):



    
    usuario = request.user
    compras = User_Sales.objects.get(user=usuario)
    
    
    if compras:
    
    
        sales = User_Sales.objects.all()
    
    

    return render(request, 'meus-pedidos.html', {'sales':sales, 'STATIC_URL': settings.STATIC_URL})        



def login(request, template_name="login2.html"):

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST) # Veja a documentacao desta funcao
        
        if form.is_valid():
            
            User(request, form.get_user())
            return HttpResponseRedirect("/?next=%s") # redireciona o usuario logado para a pagina inicial
        else:
            return render(request, "login2.html", {"form": form})
    
    #se nenhuma informacao for passada, exibe a pagina de login com o formulario
    return render(request, template_name, {"form": AuthenticationForm(),'STATIC_URL': settings.STATIC_URL})

