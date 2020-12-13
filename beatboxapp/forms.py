from django.forms import *
from .models import *
from db_file_storage.form_widgets import DBClearableFileInput
class Musica(ModelForm):
    class Meta:
        model = musica
        fields = "__all__"
        exclude = []
        widgets = {"imagem":DBClearableFileInput,"video":DBClearableFileInput}
class Studio(ModelForm):
    class Meta:
        model = studio
        fields = "__all__"
        widgets = {"imagem":DBClearableFileInput}
class Cantor(ModelForm):
    class Meta:
        model = cantor
        fields = "__all__"
        widgets = {"imagem":DBClearableFileInput}
class Loja(ModelForm):
    class Meta:
        model = loja
        fields = "__all__"
        widgets = {"imagem":DBClearableFileInput}
