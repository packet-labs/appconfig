from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import HttpResponse

from .models import Node

import string
from random import randint,choice
from passlib.context import CryptContext

from esxicfg.forms import RequestedConfigForm

def index(request):
    template = loader.get_template('esxicfg/mainpage.html')
    context = {

    }
    return HttpResponse(template.render(context, request))

def buildconfig(request):
    if request.method == "POST":
        form = RequestedConfigForm(request.POST)
        if form.is_valid():
            template = loader.get_template('esxicfg/success.html')
            allchar = string.ascii_letters + string.punctuation + string.digits
            password = "".join(choice(allchar) for x in range(randint(8, 12)))
            myctx = CryptContext(schemes=["md5_crypt"])
            password_hash = myctx.hash(password)
            newNode = Node(password_hash=password_hash, network_autoconfig=request.POST['NetworkMode'], network_vlan=request.POST['NetworkVLAN'], network_manualip=request.POST['NetworkIP'], network_manualnm=request.POST['NetworkNM'], network_manualgw=request.POST['NetworkGW'], ssh_config=request.POST['SSHmode'])
            newNode.save()
            context = {
                'password': password,
                'node_id': newNode.id
            }
            return HttpResponse(template.render(context, request))
        else:
            template = loader.get_template('esxicfg/mainpage.html')
            context = {
                error_message: 'Invalid options, please try again.'
            }
            return HttpResponse(template.render(content, request))
    else:
        template = loader.get_template('esxicfg/mainpage.html')
        context = {
            error_message: 'Form input are required.'
        }
        return HttpResponse(template.render(content, request))


def ipxe(request, node_id):
    template = loader.get_template('esxicfg/ipxe-65.txt')
    context = {
        'node_id': node_id
    }
    return HttpResponse(template.render(context, request), content_type="text/plain")

def bootcfg(request, node_id):
    template = loader.get_template('esxicfg/bootcfg-65.txt')
    context = {
        'node_id': node_id
    }
    return HttpResponse(template.render(context, request), content_type="text/plain")

def kscfg(request, node_id):
    template = loader.get_template('esxicfg/kscfg-65.txt')
    try:
        data = Node.objects.get(id=node_id)
    except:
        return HttpResponse("404")
    else:
        context = {
            'node_id': node_id,
            'data': data
        }
        return HttpResponse(template.render(context, request), content_type="text/plain")
