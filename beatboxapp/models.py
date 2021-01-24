from django.db.models import *
from db_file_storage.model_utils import delete_file, delete_file_if_needed
from django.utils import timezone
class video(Model):
    byte = TextField()
    filename = CharField(max_length=300)
    mimetype = CharField(max_length=300)
class audio(Model):
    byte = TextField()
    filename = CharField(max_length=300)
    mimetype = CharField(max_length=300)
class imagem(Model):
    byte = TextField()
    filename = CharField(max_length=300)
    mimetype = CharField(max_length=300)

class musica(Model):
    titulo = CharField(verbose_name="titulo",default="",max_length=200,blank=False,null=False)
    data_de_criacao = DateTimeField(verbose_name="data_de_criacao",auto_now_add=True)
    tipo = CharField(verbose_name="tipo",max_length=150,default=" ",blank=False,null=False)
    sobre = TextField(verbose_name="sobre",default="A melhor musica de sempre",blank=True,null=False)
    artistas = CharField(verbose_name="artistas",max_length=150,default="",blank=False,null=False)
    slug = SlugField(verbose_name="slug",max_length=500,default="ksDI8lkdlaskldkslkasdlkslsdakl9dsdjK",blank=True,null=False)
    video = FileField(verbose_name="video",blank=True,null=False,upload_to="beatboxapp.video/byte/filename/mimetype")
    audio = FileField(verbose_name="audio",blank=True,null=False,upload_to="beatboxapp.audio/byte/filename/mimetype")
    imagem = ImageField(verbose_name="imagem",blank=True,null=False,upload_to="beatboxapp.imagem/byte/filename/mimetype")
    duracao = CharField(verbose_name="duracao",max_length=150,default="",blank=True,null=False)
    de = PositiveIntegerField(verbose_name="de",default=0,blank=True,null=False)
    downloads = PositiveIntegerField(verbose_name="downloads",default=0,blank=True,null=False)
    denuncias = PositiveIntegerField(verbose_name="denuncias",default=0,blank=True,null=False)
    gostos = PositiveIntegerField(verbose_name="gostos",default=0,blank=True,null=False)
    def __str__(self):
        return str(self.artistas) + " :" + str(self.titulo)
    def save(self, *args, **kwargs):
            delete_file_if_needed(self, 'imagem')
            delete_file_if_needed(self, 'video')
            delete_file_if_needed(self, 'audio')
            super(musica, self).save(*args, **kwargs)
    def delete(self, *args, **kwargs):
            super(musica, self).delete(*args, **kwargs)
            delete_file(self, 'imagem')
            delete_file(self, 'video')
            delete_file(self, 'audio')
class cantor(Model):
    sexo = CharField(verbose_name="sexo",default="Masculino",choices=(("Masculino","Masculino"),("Feminino","Feminino")),max_length=15,blank=False,null=False)
    confirmed_contacto = BooleanField(default=False,null=False)
    confirmed_email = BooleanField(default=False,null=False)
    confirme_contacto = PositiveIntegerField(verbose_name="confirme_contacto",default=0,blank=True,null=False)
    confirme_email = PositiveIntegerField(verbose_name="confirme_email",default=0,blank=True,null=False)
    password = CharField(verbose_name="password",default="",max_length=200,blank=False,null=False)
    pr_nome = CharField(verbose_name="pr_nome",default="",max_length=200,blank=False,null=False)
    ul_nome = CharField(verbose_name="ul_nome",default="",max_length=200,blank=False,null=False)    
    contacto = CharField(verbose_name="contacto",default="+258",max_length=15,blank=False,null=False)
    email = EmailField(verbose_name="email",max_length=50,blank=True,null=False)
    links = CharField(verbose_name="links",default="",max_length=500,blank=True,null=False)
    data_de_nascimento = DateField(verbose_name="data_de_nascimento",blank=False,null=False)
    sobre = TextField(verbose_name="sobre",default="A/O melhor artista de sempre",blank=True,null=False)
    data_de_criacao = DateTimeField(verbose_name="data_de_criacao",auto_now_add=True)
    imagem = ImageField(verbose_name="imagem",blank=True,null=False,upload_to="beatboxapp.imagem/byte/filename/mimetype")
    denuncias = PositiveIntegerField(verbose_name="denuncias",default=0,blank=True,null=False)
    gostos = PositiveIntegerField(verbose_name="gostos",default=0,blank=True,null=False)
    slug = SlugField(verbose_name="slug",max_length=500,default="jkjsuisUIUS8d78sd87as",blank=True,null=False)
    pais = CharField(verbose_name="pais",default="",max_length=200,blank=False,null=False)
    def __str__(self):
        return self.pr_nome + " " + self.ul_nome
    def save(self, *args, **kwargs):
            delete_file_if_needed(self, 'imagem')
            super(cantor, self).save(*args, **kwargs)
    def delete(self, *args, **kwargs):
            super(cantor, self).delete(*args, **kwargs)
            delete_file(self, 'imagem')
class loja(Model):
    nome = CharField(verbose_name="nome",default="",max_length=200,blank=False,null=False)
    pais = CharField(verbose_name="pais",default="",max_length=200,blank=False,null=False)
    data_de_criacao = DateTimeField(verbose_name="data_de_criacao",auto_now_add=True)
    contacto = CharField(verbose_name="contacto",default="+258",max_length=15,blank=False,null=False)
    imagem = ImageField(verbose_name="imagem",blank=True,null=False,upload_to="beatboxapp.imagem/byte/filename/mimetype")
    sobre = TextField(verbose_name="sobre",default="O melhor studio de sempre",blank=True,null=False)
    provincia = CharField(verbose_name="provincia",default="",max_length=200,blank=False,null=False)
    cidade = CharField(verbose_name="cidade",default="",max_length=200,blank=False,null=False)
    de = PositiveIntegerField(verbose_name="de",default=0,blank=True,null=False)
    email = EmailField(verbose_name="email",max_length=50,blank=True,null=False)
    localizacao = CharField(verbose_name="localizacao",default="",max_length=200,blank=False,null=False)
    denuncias = PositiveIntegerField(verbose_name="denuncias",default=0,blank=True,null=False)
    gostos = PositiveIntegerField(verbose_name="gostos",default=0,blank=True,null=False)
    slug = SlugField(verbose_name="slug",max_length=500,default="jdkuuad8a98d98a8uasuuida",blank=True,null=False)
    def __str__(self):
        return self.nome
    def save(self, *args, **kwargs):
            delete_file_if_needed(self, 'imagem')
            super(loja, self).save(*args, **kwargs)
    def delete(self, *args, **kwargs):
            super(loja, self).delete(*args, **kwargs)
            delete_file(self, 'imagem')
class studio(Model):
    nome = CharField(verbose_name="nome",default="",max_length=200,blank=False,null=False)
    pais = CharField(verbose_name="pais",default="",max_length=200,blank=False,null=False)
    data_de_criacao = DateTimeField(verbose_name="data_de_criacao",auto_now_add=True)
    contacto = CharField(verbose_name="contacto",default="+258",max_length=15,blank=False,null=False)
    email = EmailField(verbose_name="email",max_length=50,blank=True,null=False)
    imagem = ImageField(verbose_name="imagem",blank=True,null=False,upload_to="beatboxapp.imagem/byte/filename/mimetype")
    sobre = TextField(verbose_name="sobre",default="O melhor studio de sempre",blank=True,null=False)
    provincia = CharField(verbose_name="provincia",default="",max_length=200,blank=False,null=False)
    cidade = CharField(verbose_name="cidade",default="",max_length=200,blank=False,null=False)
    de = PositiveIntegerField(verbose_name="de",default=0,blank=True,null=False)
    slug = SlugField(verbose_name="iklsdkl",max_length=500,default="jkjkdjsajdkjajasdkjanhdja",blank=True,null=False)
    localizacao = CharField(verbose_name="localizacao",default="",max_length=200,blank=False,null=False)
    denuncias = PositiveIntegerField(verbose_name="denuncias",default=0,blank=True,null=False)
    gostos = PositiveIntegerField(verbose_name="gostos",default=0,blank=True,null=False)
    def __str__(self):
        return self.nome
    def save(self, *args, **kwargs):
            delete_file_if_needed(self, 'imagem')
            super(studio, self).save(*args, **kwargs)
    def delete(self, *args, **kwargs):
            super(studio, self).delete(*args, **kwargs)
            delete_file(self, 'imagem')
class notificacao(Model):
    conteudo = TextField()
    data_de_criacao = DateTimeField(auto_now_add=True)
    para = PositiveIntegerField(verbose_name="para",default=0,blank=True,null=False)
    slug = SlugField(verbose_name="slug",max_length=500,default="hjahjjdhjh",blank=True,null=False)
class ajuda(Model):
    tema = CharField(max_length=200,blank=False,null=False)
    data_de_criacao = DateTimeField(verbose_name="data_de_criacao",auto_now_add=True)
    dica = TextField(blank=False,null=False)
    link = CharField(max_length=300,blank=False,null=False)
    slug = SlugField(verbose_name="slug",max_length=500,default="iklsdkl",blank=True,null=False)
r = (("musica","musica"),("cantor","cantor"),("studio","studio"),("loja","loja"))
class denuncia(Model):
    to = CharField(verbose_name="to",default="musica",choices=r,max_length=200,blank=False,null=False)
    para = PositiveIntegerField(verbose_name="para",default=0,blank=True,null=False)
    sobre = TextField(blank=False,null=False)
    data_de_criacao = DateTimeField(verbose_name="data_de_criacao",auto_now_add=True)
class terms(Model):
    tema = CharField(max_length=200,blank=False,null=False)
    sobre = TextField(blank=False,null=False)
# Create your models here.
#class anuncio(Model):
#    qual = ForeignKey(studio)
