from django.shortcuts import render
from django.conf import settings
# Create your views here.


def home(request):

    context = {'STATIC_URL': settings.STATIC_URL}
    return render(request, 'index.html', context)
