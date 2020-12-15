from django.contrib import admin
from django.forms import *
from .models import *
from db_file_storage.form_widgets import DBAdminClearableFileInput
class Musica(ModelForm):
    class Meta:
        model = musica
        fields = "__all__"
        exclude = []
        widgets = {"imagem":DBAdminClearableFileInput,"video":DBAdminClearableFileInput}
class Studio(ModelForm):
    class Meta:
        model = studio
        fields = "__all__"
        widgets = {"imagem":DBAdminClearableFileInput}
class Cantor(ModelForm):
    class Meta:
        model = cantor
        fields = "__all__"
        widgets = {"imagem":DBAdminClearableFileInput}
class Loja(ModelForm):
    class Meta:
        model = loja
        fields = "__all__"
        widgets = {"imagem":DBAdminClearableFileInput}
class MusicaAdmin(admin.ModelAdmin):
    form = Musica

class StudioAdmin(admin.ModelAdmin):
    form = Studio
class CantorAdmin(admin.ModelAdmin):
    form = Cantor
class LojaAdmin(admin.ModelAdmin):
    form = Loja
admin.site.register(ajuda)
admin.site.register(musica)
admin.site.register(cantor)
admin.site.register(studio)
admin.site.register(loja)
admin.site.register(notificacao)
admin.site.register(denuncia)
admin.site.register(terms)
# Register your models here.
