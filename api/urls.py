from django.conf.urls import url
from .views import *

urlpatterns = [
    url('vagas$', VagaList.as_view()),
    url('empresas$', EmpresaList.as_view()),
    url('vagas/(?P<pk>[0-9]+)$', VagaDetalhes.as_view()),
    url('empresas/(?P<pk>[0-9]+)$', EmpresaDetralhes.as_view()),
]