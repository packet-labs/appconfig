import uuid
from django.db import models

class Node(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    password_hash = models.CharField(max_length=100)
    network_autoconfig = models.IntegerField(default=1)
    network_vlan = models.IntegerField(null=True)
    network_manualip = models.CharField(max_length=15,default="")
    network_manualnm = models.CharField(max_length=15,default="")
    network_manualgw = models.CharField(max_length=15,default="")
    ssh_config = models.IntegerField(default=0)

