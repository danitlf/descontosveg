"""descontosveg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



from django.conf.urls import url
from django.contrib import admin
from descontosveg.book import views
from descontosveg.moip import views as view_moip
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^moip/(\d)$', view_moip.moipSend, name='moipSend'),
    url(r'^moip/response/$', view_moip.moipResponse, name='moipSend'),
    url(r'^formmoip/$', view_moip.formMoip, name='formMoip'),
    url(r'^send_email/$', views.send_email, name='send_email'),
    url(r'^cadastro/$', views.cadastro, name='cadastro'),
    url(r'^pedidos/$', views.pedidos, name='pedidos'),
    url(r'^contato/$', views.contato, name='contato'),
    url(r'^sobre/$', views.sobre, name='sobre'),
    

    url(r'^login/$', auth_views.login, {'template_name': 'login2.html'}),

    url(r'^logout/$', auth_views.logout, name='logout'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()


admin.site.site_header = settings.ADMIN_SITE_HEADER

