from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('buildconfig', views.buildconfig, name='buildconfig'),
    path('ipxe/<uuid:node_id>', views.ipxe, name='ipxe'),
    path('esxibootcfg/<uuid:node_id>', views.bootcfg, name='bootcfg'),
    path('esxiks/<uuid:node_id>', views.kscfg, name='kscfg'),
]

