from django.template import Library
from django.template.defaultfilters import stringfilter
register = Library()
from ..models import *
import random

@register.filter(is_safe=True)
@stringfilter
def st(value):
    value = str(value)
    return len(value)
#@register.filter(is_safe=True)
def gRan():
    if len(studio.objects.all()) > 1 and len(loja.objects.all()) > 1:
        l = random.randrange(1,2)
        if l == 1:
            l = random.randrange(1,len(studio.objects.all()))
            return studio.objects.filter(id=l).first()
        elif l == 2:
            l = random.randrange(1,len(loja.objects.all()))
            return loja.objects.filter(id=l).first()
        else:
            return {"slug":"","nome":"Nenhum publicado"}
    elif len(studio.objects.all()) > 1:
        l = random.randrange(1,len(studio.objects.all()))
        return studio.objects.filter(id=l).first()
    elif len(loja.objects.all()) > 1:
        l = random.randrange(1,len(loja.objects.all()))
        return loja.objects.filter(id=l).first()
    else:
        return {"slug":"","nome":"Nenhum publicado"}
@register.filter(is_safe=True)
def qumus(value):
    value = int(value)
    ca = cantor.objects.filter(id=value).first()
    if ca != None:
        return len(musica.objects.filter(de=ca.id).all())
    else:
        return 0
