from django import forms

class RequestedConfigForm(forms.Form):
    NetworkModeChoices = (
        ('0', 'No Autoconfig'),
        ('1', 'DHCP'),
        ('2', 'Private IP only'),
        ('3', 'Public IP only'),
        ('4', 'Public IP with management vmkernel1')
    )
    SSHmodeChoices = (
        ('0', 'Disabled'),
        ('1', 'Enabled'),
        ('2', 'Enabled, keys only')
    )
    ESXiVersionChoices = (
	('0', '6.5.0-20180304001'),
	('1', '6.5.0-20181104001'),
	('2', '6.7.0-20181104001')
    )
    NetworkMode = forms.TypedChoiceField(choices=NetworkModeChoices,coerce=int)
    NetworkVLAN = forms.IntegerField(min_value=0, max_value=4096)
    NetworkIP = forms.GenericIPAddressField(protocol="IPv4")
    NetworkNM = forms.GenericIPAddressField(protocol="IPv4")
    NetworkGW = forms.GenericIPAddressField(protocol="IPv4")
    SSHmode = forms.TypedChoiceField(choices=SSHmodeChoices,coerce=int)
    ESXiVersion = forms.TypedChoiceField(choices=ESXiVersionChoices,coerce=int)
