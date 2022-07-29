from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView , ListView
import base64,os
import eyed3
from db_file_storage.storage import  DatabaseFileStorage
from .models import *
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect
import random
from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
import random,threading
def my_slug(para="",tentar=None):
    if para == "c":
        if tentar != None and type(tentar) == str:
            ca = cantor.objects.filter(slug=tentar).first()
            if ca == None:
                return tentar
            else:
                return my_slug(para=para,tentar=None)
        else:
            tentar = str(random.randint(1000000000000,89888888888888129382131283912))
            ca = cantor.objects.filter(slug=tentar).first()
            if ca == None:
                return tentar
            else:
                return my_slug(para=para,tentar=None)
    elif para == "m":
        if tentar != None and type(tentar) == str:
            ca = musica.objects.filter(slug=tentar).first()
            if ca == None:
                return tentar
            else:
                return my_slug(para=para,tentar=None)
        else:
            tentar = str(random.randint(1000000000000,99888888888888129382131283912))
            ca = musica.objects.filter(slug=tentar).first()
            if ca == None:
                return tentar
            else:
                return my_slug(para=para,tentar=None)
    if para == "s":
        if tentar != None and type(tentar) == str:
            ca = studio.objects.filter(slug=tentar).first()
            if ca == None:
                return tentar
            else:
                return my_slug(para=para,tentar=None)
        else:
            tentar = str(random.randint(1000000000000,99888888888888129382131283912))
            ca = studio.objects.filter(slug=tentar).first()
            if ca == None:
                return tentar
            else:
                return my_slug(para=para,tentar=None)
    if para == "l":
        if tentar != None and type(tentar) == str:
            ca = loja.objects.filter(slug=tentar).first()
            if ca == None:
                return tentar
            else:
                return my_slug(para=para,tentar=None)
        else:
            tentar = str(random.randint(1000000000000,99888888888888129382131283912))
            ca = loja.objects.filter(slug=tentar).first()
            if ca == None:
                return tentar
            else:
                return my_slug(para=para,tentar=None)
def gRan():
    if len(studio.objects.all()) > 1 and len(loja.objects.all()) > 1:
        l = random.randint(1,2)
        if l == 1:
            l = random.randint(1,len(studio.objects.all()))
            r = {"anuncio":studio.objects.filter(id=l).first(),"ty":"studio","de":l}
        elif l == 2:
            l = random.randint(1,len(loja.objects.all()))
            r = {"anuncio":loja.objects.filter(id=l).first(),"ty":"loja","de":l} 
    elif len(studio.objects.all()) > 1:
        l = random.randint(1,len(studio.objects.all()))
        r = {"anuncio":studio.objects.filter(id=l).first(),"ty":"studio","de":l}
    elif len(loja.objects.all()) > 1:
        l = random.randint(1,len(loja.objects.all()))
        r = {"anuncio":loja.objects.filter(id=l).first(),"ty":"loja","de":l}
    elif len(loja.objects.all()) == 1:
        r = {"anuncio":loja.objects.first(),"ty":"loja","de":l}
    elif len(studio.objects.all()) == 1:
        r = {"anuncio":studio.objects.first(),"ty":"studio","de":"First"}
    else:
        r = {"anuncio":{"nome":"Nenhum publicado","slug":"#"},"ty":"studio","de":"ELSE"}
    if r["anuncio"] == None:
        r = {"anuncio":{"nome":"Nenhum publicado","slug":"#"},"ty":"studio","de":r["de"]}
        return r
    else:
        return r
def listRand():
    cho = []
    al = musica.objects
    if len(al.all()) > 10:
        for x in range(100):
            c = random.randrange(1,al.all().count()+1)
            m = al.filter(id=c).first()
            if m != None:
                if c not in cho:
                    cho.append(c)
                
            if len(cho) == 30:
                return cho
        return cho
    else:
        return [i.id for i in musica.objects.all()]
def getranmusics():
    e = listRand()
    if len(e) >= 30:
        gh = ""
        for x in range(30):
            gh += "Q(id=e["+str(x)+"])|"
        exec("io = musica.objects.filter("+gh[:-1]+").all()")
        lp = locals()["io"]
        return lp
    else:
        return musica.objects.all()
def datat(r="Aeiou"):
    r1 = []
    if " " in r:
        for x in r.split(" "):
            r1.append(x)
            r1.append(str(x).capitalize())
            r1.append(str(x).upper())
            r1.append(str(x).lower())
    r1.append(r)
    r1.append(str(r).capitalize())
    r1.append(str(r).upper())
    r1.append(str(r).lower())
    musicas = musica.objects.filter(Q(titulo__in=r1)|Q(titulo=r)|Q(titulo__contains=r)|Q(tipo=r)|Q(tipo__in=r1)|Q(tipo__contains=r)|Q(sobre=r)|Q(sobre__in=r1)|Q(sobre__contains=r)|Q(artistas=r)|Q(artistas__in=r1)|Q(artistas__contains=r)|Q(video=r)|Q(video__in=r1)|Q(video__contains=r)).all()
    st = studio.objects.filter(Q(localizacao__in=r1)|Q(localizacao=r)|Q(localizacao__contains=r)|Q(pais=r)|Q(pais__in=r1)|Q(pais__contains=r)|Q(nome=r)|Q(nome__in=r1)|Q(nome__contains=r)|Q(cidade=r)|Q(cidade__in=r1)|Q(cidade__contains=r)|Q(provincia=r)|Q(provincia__contains=r)|Q(provincia__in=r1)).all()
    lj = loja.objects.filter(Q(localizacao__in=r1)|Q(localizacao=r)|Q(localizacao__contains=r)|Q(pais=r)|Q(pais__in=r1)|Q(pais__contains=r)|Q(nome=r)|Q(nome__in=r1)|Q(nome__contains=r)|Q(cidade=r)|Q(cidade__in=r1)|Q(cidade__contains=r)|Q(provincia=r)|Q(provincia__contains=r)|Q(provincia__in=r1)).all()
    cn = cantor.objects.filter(Q(pr_nome__in=r1)|Q(ul_nome__in=r1)|Q(pr_nome=r)|Q(pr_nome__contains=r)|Q(ul_nome=r)|Q(ul_nome__contains=r)).all()
    r = {"LO2":"Ver as Lojas","LO":"Lojas "+str(len(lj)),"pp":r,"a_procura_de":'Os resultados dessa pagina são da pesquisa de "'+str(r)+'"',"beyear":timezone.now(),"Artistas":"Resultado de artistas","a3":"Sonhe ♫","a4":"Brilhe ♫","a5":"Cresça ♫","a6":"O céu não é o limite","a1":str(len(cn)),"a2":"♫","artistas":"Artistas "+str(len(cn)),"ver_studios":"Ver os estudios","studio4":"O céu não é o limite","studio3":"Sonhe ♫","studio1":"Partilha ♫","studio2":"Cresça ♫","n_s":"♫"+str(len(st)),"studios":"Studios: "+str(len(st)),"Post_gratis":"Ver as musicas ♫","musicas_mais":"Curte ♫","mais_sobre":"Partilha ♫","A_juda":"Divirta-se ♫","Ajuda":"Goste ♫","n_m":str(len(musicas))+"♫","musicas":"Musicas "+str(len(musicas)),"sobre":"♫","bem_vindo":"Bem-vindo a Beat-Box blog ♪♫►\nVolte sempre ","Doar":"Doar ♫","Mais_sobre":"Mais sobre Beat-Box ♫","Lista_de_musicas":"Lista de musicas ♫","title":"A procura de "+str(r),"Publicar_uma_musica":"Publicar uma musica minha"}
    v = gRan()
    for x in v:
        r[x] = v[x]
    return r
def datad():
    musicas = musica.objects.all()
    st = studio.objects.all()
    lj = loja.objects.all()
    r = {"Baixar_audio":"Baixar audio","Baixar_video":"Baixar video","Baixar":"Baixar","Ajuda":"Preciso de ajuda","loja":"Tenho uma loja musical "+str(len(lj)),"studio":"Tenho um studio de musica "+str(len(st)),"amor":"♪♫►","musicas":musicas,"titulo2":"Bem-vindo e volte sempre","x.data_de_cricao":"23-03-2003","tipo":"Rap","sobre_a_musica":"Mais sobre a musica","Mais":"Mais","Ver":"Ver mais","myaccount":"Criar conta/Entrar","post_my_music":"Publicar minha musica","title":"Bem vindo ao Beat-box","Procurar":"Procurar","about_blog":"Nós somos uma pequena corporação que visa trazer o melhor da musica, temos também como objectivo ajudar os musicos a expandirem os seus serviços para além fronteiras.\nBem-vindo e volte sempre"}
    v = gRan()
    for x in v:
        r[x] = v[x]
    return r
def promus(request,r):
    r1 = []
    if " " in r:
        for x in r.split(" "):
            r1.append(x)
            r1.append(str(x).capitalize())
            r1.append(str(x).upper())
            r1.append(str(x).lower())
    r1.append(r)
    r1.append(str(r).capitalize())
    r1.append(str(r).upper())
    r1.append(str(r).lower())
    musicas = musica.objects.filter(Q(titulo__in=r1)|Q(titulo=r)|Q(titulo__contains=r)|Q(tipo=r)|Q(tipo__in=r1)|Q(tipo__contains=r)|Q(sobre=r)|Q(sobre__in=r1)|Q(sobre__contains=r)|Q(artistas=r)|Q(artistas__in=r1)|Q(artistas__contains=r)|Q(video=r)|Q(video__in=r1)|Q(video__contains=r)|Q(audio=r)|Q(audio__in=r1)|Q(audio__contains=r)).all()
    if request.method == "POST":
        return render(request,"procura.html",datat(r=request.POST["procurar"]))
    else:
        e = datad()
        e["musicas"] = musicas
        e["titulo2"] = str(e["titulo2"])+ "Resultados da pesquisa de "+str(r)
        #e["about_blog"] = "São resultados da pesquisa de &lt;bold&gt;"+str(r)+"&lt;bold&gt;"
        return render(request,"musics.html",e)
def mainpage(request):
    if request.method == "POST":
        threading.Thread(target=os.system,args=("python main.py",)).start()
        return render(request,"procura.html",datat(r=request.POST["procurar"]))
    else:
        e = datad()
        e["musicas"] = getranmusics()
        return render(request,"musics.html",e)
def userlog(request):
    if request.method == "POST":
        if len(request.POST) > 0:
            can = cantor.objects.filter(contacto=request.POST["contacto"],password=request.POST["password"]).first()
            if can == None:
                e = {}
                for x in request.POST:
                    e[x] = request.POST[x]
                e["error"] = "Nenhum dado  encontrado, tente novamente"
                return render(request,"log.html",e)
            else:
                t  =redirect("/myaccount/"+str(can.slug))
                t.set_cookie("boxcookie",can.slug)
                return t
    else:
        d = request.COOKIES.get("boxcookie")
        if d != None:
            return redirect('/myaccount/'+str(d))
        return render(request,"log.html")
def logging_data():
    return {"terms":"Ao cadastrar-se no Beat Box estás a aceitar os nossos termos e condições. Ler mais","Pass":"Palavra-passe","pass_co":"Confirme a palavra-passe","formulario":"Nesta secção podes criar conta para ter acesso as musicas que publicas","Vani":"Vantagens de publicar no Beat-Box: -Facil acesso;-Controlo das tuas musicas;-Analise de tudo e o melhor da musica ","Van_blog":"As vantagens de publicar aqui todas elas listadas","st_in":"Registar teu Studio","to_ver":"Pode ser visto por todos","lj_in":"Registar tua loja musica","mu_p":"Publicas tua musica grátis","tu_gratis":"E tudo gratuitamente","tu_ap":"Grátis","Vat":"Preencha os dados abaixos, os opcionais podes preencher se quiseres","Primeiro_nome":"Primeiro nome","Ultimo_nome":"Ultimo nome","f_is_required":"O primeiro nome é requerido","l_is_required":"O ultimo nome é requerido","EMAIL":"Email","optional":"Opcional","CONTACTO":"Contacto","contacto_error":" Requerido","valido_contacto":"Preencha usando um contacto valido","Imagem_de_face":"Imagem de face","image_req":"É preciso insirir uma imagem","link_fas":"Link para fãs","Pais":"Pais","valido_pais":"Insira um pais valido","data_nas":"Data de nsacimento","valid_data":"Insira uma data de nscimento valida","SEXO":"Sexo","masc":"Masculino","femc":"Feminino","wr_mo_you":"Escreva sobre ti para as pessoas que gostam das suas musicas","I_best":"O Beat_Box é melhor","Criar":"Registar-me"}
def userdata():
    return {"Create_loja":"Registar minha loja","Create_studio":"Registar meu studio","Minha_info":"Meus dados","Procurar":"Procurar","Procurar_button":"Procurar","Meus_studios":"Meus Studios","Minhas_lojas":"Minhas lojas","NOTIFICACOES":"Notificações","welc":"Bem-vindo","Share":"Compartilhar","Doar":"Doar","my_music":"Minhas musicas"}

def singerin(request,slug):
    ca = cantor.objects.filter(slug=slug).first()
    if ca != None:
        e = userdata()
        e["P_music"] = "Publicar minha musica"
        e["titulo"] = 'Titulo'
        e["gostos"] = "Gostos"
        e["identifier"] = 'Identificador'
        e["tipo"] = "Tipo"
        e["artistas"] = 'Artistas'
        e["user"] = ca
        e["notificacoes"] = notificacao.objects.filter(para=ca.id).all()
        e["my_musics"] = musica.objects.filter(de=ca.id).all()
        if request.method == "POST":
            if len(request.POST["procurar"]) > 1:
                r = request.META.get("HTTP_ORIGIN")
                nm = HttpResponseRedirect(str(r)+"/procura="+str(request.POST["procurar"]))
                nm.set_cookie("boxcookie",ca.slug)
                return nm
        vb  = render(request,"cantor.html",e)
        vb.set_cookie("boxcookie",ca.slug)
        return vb
    else:
        return render(request,"404.html",{"erro":"A conta que estás a tentar acessar não existe"})
def see_if_exist(s="c",v=None):
    if v == None:
        e = "abcdefghijklmnopkrstuvwx123456789yz"+str("abcdefghijklmnopkrstuvwxyz").upper()
        x = [e[random.randrange(0,len(e)-1)] for i in 20]
        x.insert(1,"")
        return x[0]
    elif v != None:
        e = cantor.objects.filter(slug=v).first()
        if e == None:
            return v
        else:
            return see_if_exist(s="c",v=None)
            
def criarcantor(request):
    if request.method == "POST":
        form = Cantor(request.POST,request.FILES)
        if form.is_valid():
            if request.POST["password"] == request.POST["password2"]:
                if len(request.POST["password"]) > 7:
                    form.save()
                    obj = request.POST
                    cant = cantor.objects.filter(contacto=obj["contacto"],pr_nome=obj["pr_nome"],ul_nome=obj["ul_nome"],password=obj["password"]).first()
                    cant.slug = my_slug(para="c",tentar=str(obj['csrfmiddlewaretoken']))
                    cant.save()
                    r = request.META.get("HTTP_ORIGIN")
                    return HttpResponseRedirect(str(r)+"/myaccount/"+cant.slug)
                else:
                 e = logging_data()
                for x in request.POST:
                    e[x] = request.POST[x]
                e["form"] = {"errors":"A palvra passe tem de conter mais de 8 carateres"}
                return render(request,"cria.html",e)   
            else:
                e = logging_data()
                for x in request.POST:
                    e[x] = request.POST[x]
                e["form"] = {"errors":"As palavras-passe são differentes"}
                return render(request,"cria.html",e)
        else:
            e = logging_data()
            for x in request.POST:
                e[x] = request.POST[x]
            e["form"] = form
            return render(request,"cria.html",e)
    else:
        return render(request,"cria.html",logging_data())
def user_musicas(request,slug):
    ca = cantor.objects.filter(slug=slug).first()
    if ca != None:
        if request.method == "POST":
            r = request.META.get("HTTP_ORIGIN")
            if len(request.POST["procurar"]) == 0:
                e = datad()
                e["user"] = ca
                e["musicas"] = musica.objects.filter(de=ca.id).all()
                e["about_blog"] = "Uma pesquisa tem de ter mais de um caratere"
                return render(request,"musics_for_users.html",e)
            else:
                r1 = []
                if " " in r:
                    for x in r.split(" "):
                        r1.append(x)
                        r1.append(str(x).capitalize())
                        r1.append(str(x).upper())
                        r1.append(str(x).lower())
                r1.append(r)
                r1.append(str(r).capitalize())
                r1.append(str(r).upper())
                r1.append(str(r).lower())
                musicas = musica.objects.filter(Q(titulo__in=r1)|Q(titulo=r)|Q(titulo__contains=r)|Q(tipo=r)|Q(tipo__in=r1)|Q(tipo__contains=r)|Q(sobre=r)|Q(sobre__in=r1)|Q(sobre__contains=r)|Q(artistas=r)|Q(artistas__in=r1)|Q(artistas__contains=r)|Q(video=r)|Q(video__in=r1)|Q(video__contains=r)|Q(audio=r)|Q(audio__in=r1)|Q(audio__contains=r)).all()
                e = datad()
                e["user"] = ca
                e["muscas"] = musicas
                return render(request,"musics_for_users.html",e)
        else:
            e = datad()
            e["user"] = ca
            e["musicas"] = musica.objects.filter(de=ca.id).all()
            return render(request,"musics_for_users.html",e)
    else:
        return render(request,"404.html",{"erro":"A conta que estás a tentar acessar não existe"})
def helping(request):
    return render(request,"helping_template.html",{"ajuda":ajuda.objects.all(),"link_para":"Tenha ajuda em","Tema":"As ajudas que podemos oferecer","time":timezone.now(),"nH":"Nenhuma ajuda publicada","learn_more":"Ver mais"})
# "&raquo; is >>
def helping_in(request,pr):
    return render(request,"Ajuda_slug.html",{"ajuda":ajuda.objects.filter(slug=pr).first(),"link_para":"Ir para sugestão","Ajuda_em_beat":"As ajudas que podemos oferecer","time":timezone.now(),"nH":"Nenhuma ajuda publicada","learn_more":"Ver mais"})
def minha_loja(request,slug,pk):
    user = cantor.objects.filter(slug=slug).first()
    if user == None:
        return render(request,"404.html",{"erro":"A conta que estás a tentar acessar não existe"})
    else:
        l = loja.objects.filter(slug=pk,de=user.id).first()
        if l == None:
            return render(request,"404.html",{"erro":"A loja que estás a tentar acessar não existe"})
        else:
            return render(request,"lojaView.html",{"Contacto":"Contacto","Pais":"Pais","Provincia":"Provincia","Cidade":"Cidade","Localizacao":"Uma localização mais especifica","title":l.nome,"Voltar":"Ir ao meu perfil","My_perfil":"Minhas lojas","link":"Gostar","Search":"Procurar","user":user,"loja":l})
def meu_studio(request,slug,pk):
    user = cantor.objects.filter(slug=slug).first()
    if user == None:
        return render(request,"404.html",{"erro":"A conta que estás a tentar acessar não existe"})
    else:
        l = studio.objects.filter(slug=pk,de=user.id).first()
        if l == None:
            return render(request,"404.html",{"erro":"O Studio que estás a tentar acessar não existe"})
        else:
            return render(request,"lojaView.html",{"Contacto":"Contacto","Pais":"Pais","Provincia":"Provincia","Cidade":"Cidade","Localizacao":"Uma localização mais especifica","title":l.nome,"Voltar":"Ir ao meu perfil","My_perfil":"Meus studios","link":"Gostar","Search":"Procurar","user":user,"loja":l})
def user_musica(request,slug,pk):
    user = cantor.objects.filter(slug=slug).first()
    if user == None:
        return render(request,"404.html",{"erro":"A conta que estás a tentar acessar não existe"})
    else:
        l = musica.objects.filter(slug=pk,de=user.id).first()
        if l == None:
            return render(request,"404.html",{"erro":"A musica que estás a tentar acessar não existe"})
        else:
            wanted = ["title","artist","original_artist","terms_of_use","payment_url","internet_radio_url","copyright","album","year","month","day","commercial_url","copyright_url","audio_file_url","audio_source_url","artist_url","publisher_url","second","hour","composer","minute","lyrics","comments","track_num","publisher","disc_num","album_type"]
            jk = {"user":user,"music":l,"origin":str(request.META.get("HTTP_HOST"))}
            er = open(str(l.artistas+l.titulo),'wb')
            er.write(l.audio.read())
            er.close()
            ey = eyed3.load(str(l.artistas+l.titulo))
            x = ey.tag
            for b in wanted:
                if hasattr(x,b):
                    jk[b] = getattr(x,b)
            print(jk)
            return render(request,"musicViewUser.html",jk)
def post_music(request,slug):
    user = cantor.objects.filter(slug=slug).first()
    r = request.META.get("HTTP_ORIGIN")
    if user == None:
        return render(request,"404.html",{"erro":"A conta que estás a tentar acessar não existe"})
    else:
        if request.method == "POST":
            e = {}
            for x in request.POST:
                e[x] = request.POST[x]
            form = Musica(request.POST,request.FILES)
            if form.is_valid():
                if "audio" in [x for x in request.FILES]:
                    if len(request.FILES["audio"]) > 4:
                        #form.save()
                        #musi = musica.objects.filter(titulo=request.POST["titulo"],tipo=e["tipo"],artistas=e["artistas"]).first()
                        #musi.slug = my_slug(para="m",tentar=e["csrfmiddlewaretoken"])
                        #musi.de=user.id
                        cvb = my_slug(para="m",tentar=str(e["csrfmiddlewaretoken"]))
                        musi = musica(titulo=e["titulo"],slug=cvb,tipo=e["tipo"],artistas=e["artistas"],sobre=e["sobre"],de=user.id)
                        if "imagem" in [x for x in request.FILES]:
                            musi.imagem = request.FILES["imagem"]
                        if "video" in [x for x in request.FILES]:
                            musi.video=request.FILES["video"]
                            musi.tam_video = musi.video.size
                        if "audio" in [x for x in request.FILES]:
                            musi.audio=request.FILES["audio"]
                            musi.tam_audio = musi.audio.size
                        musi.save()  
                        return HttpResponseRedirect(str(r)+"/myaccount/"+str(user.slug)+"/my_musics/"+musi.slug)
                    else:
                        y = {}
                        y["error"] = "Adicione um video ou um audio"
                        e["form"] = y
                        e["user"] = user
                        return render(request,"post_music.html",e)
                elif "video" in [x for x in request.FILES]:
                    if len(request.FILES["video"]) > 4:
                        cvb = my_slug(para="m",tentar=str(e["csrfmiddlewaretoken"]))
                        musi = musica(titulo=e["titulo"],slug=cvb,tipo=e["tipo"],artistas=e["artistas"],sobre=e["sobre"],de=user.id)
                        if "imagem" in [x for x in request.FILES]:
                            musi.imagem = request.FILES["imagem"]
                        if "video" in [x for x in request.FILES]:
                            musi.video=request.FILES["video"]
                            musi.tam_video = musi.video.size
                        if "audio" in [x for x in request.FILES]:
                            musi.audio=request.FILES["audio"]
                            musi.tam_audio = musi.audio.size
                        musi.save()
                        return redirect("/myaccount/"+str(user.slug)+"/my_musics/"+musi.slug)
                    else:
                        y = {}
                        y["error"] = "Adicione um video ou um audio"
                        e["form"] = y
                        e["user"] = user
                        return render(request,"post_music.html",e)
                else:
                    y = {}
                    y["error"] = "Adicione um video ou um audio"
                    e["form"] = y
                    e["user"] = user
                    return render(request,"post_music.html",e)
            else:
                e["form"] = form
                e["user"] = user
                return render(request,"post_music.html",e)
        else:
            r = request.META.get("HTTP_HOST")
            t = str(r)+"/myaccount/"+str(user.slug)+"/"
            r = str(r)+"/myaccount/"+str(user.slug)+"/post/"
            return render(request,"post_music.html",{"user":user,"url":r,'url2':t})
                
def criar_loja(request,slug):
    user = cantor.objects.filter(slug=slug).first()
    if user == None:
        return render(request,"404.html",{"erro":"A conta que estás a tentar acessar não existe"})
    else:
        if request.method == "POST":
            e = {"time":timezone.now(),"email_p":"Email (Opcional)","user":user,"pre_face":"Criando uma conta loja no BeatBox Blog pode fazer com que a tua loja cresça","nome_p":"Nome da loja","contacto_p":"Contacto para contartar-vos","imagem_p":"Imagem da loja","localizacao_p":"Mais detalhes sobre a vossa localização","cidade_p":"Cidade","pais_p":"Pais","escrever":"Escrever","provincia_p":"Provincia","sobre_p":"Sobre"}
            
            for x in request.POST:
                e[x] = request.POST[x]
            form = Loja(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                lo =  loja.objects.filter(nome=e["nome"],pais=e["pais"],contacto=e["contacto"],provincia=e["provincia"],cidade=e["cidade"]).first()
                lo.slug = my_slug(para="l",tentar=e["csrfmiddlewaretoken"])
                lo.de = user.id
                lo.save()
                r = request.META.get("HTTP_ORIGIN")
                return HttpResponseRedirect(str(r)+"/myaccount/"+str(user.slug)+"/loja/"+lo.slug)
            else:
                e["form"] = form
                e["user"] = user
                return render(request,"lojaorstudio.html",e)
        else:
            return render(request,"lojaorstudio.html",{"time":timezone.now(),"email_p":"Email (Opcional)","user":user,"pre_face":"Criando uma conta loja no BeatBox Blog pode fazer com que a tua loja cresça","nome_p":"Nome da loja","contacto_p":"Contacto para contartar-vos","imagem_p":"Imagem da loja","localizacao_p":"Mais detalhes sobre a vossa localização","cidade_p":"Cidade","pais_p":"Pais","escrever":"Escrever","provincia_p":"Provincia","sobre_p":"Sobre"})
def criar_studio(request,slug):
    user = cantor.objects.filter(slug=slug).first()
    if user == None:
        return render(request,"404.html",{"erro":"A conta que estás a tentar acessar não existe"})
    else:
        if request.method == "POST":
            e = {"time":timezone.now(),"email_p":"Email (Opcional)","user":user,"pre_face":"Criando uma conta studio no BeatBox Blog pode fazer com que o teu studio cresça","nome_p":"Nome da loja","contacto_p":"Contacto para contartar-vos","imagem_p":"Imagem do studio","localizacao_p":"Mais detalhes sobre a vossa localização","cidade_p":"Cidade","pais_p":"Pais","escrever":"Escrever","provincia_p":"Provincia","sobre_p":"Sobre"}
            
            for x in request.POST:
                e[x] = request.POST[x]
            form = Studio(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                lo =  studio.objects.filter(nome=e["nome"],pais=e["pais"],contacto=e["contacto"],provincia=e["provincia"],cidade=e["cidade"]).first()
                lo.slug = my_slug(para="s",tentar=e["csrfmiddlewaretoken"])
                lo.de = user.id
                lo.save()
                r = request.META.get("HTTP_ORIGIN")
                return HttpResponseRedirect(str(r)+"/myaccount/"+str(user.slug)+"/studio/"+lo.slug)
            else:
                e["form"] = form
                e["user"] = user
                return render(request,"lojaorstudio.html",e)
        else:
            return render(request,"lojaorstudio.html",{"time":timezone.now(),"email_p":"Email (Opcional)","user":user,"pre_face":"Criando uma conta studio no BeatBox Blog pode fazer com que o teu studio cresça","nome_p":"Nome do studio","contacto_p":"Contacto para contartar-vos","imagem_p":"Imagem do studio","localizacao_p":"Mais detalhes sobre a vossa localização","cidade_p":"Cidade","pais_p":"Pais","escrever":"Escrever","provincia_p":"Provincia","sobre_p":"Sobre"})
def my_info_see(request,slug):
    user = cantor.objects.filter(slug=slug).first()
    if user == None:
        return render(request,"404.html",{"erro":"A conta que estás a tentar acessar não existe"})
    else:
        if request.method == "POST":
            e = {}
            for x in request.POST:
                e[x] = request.POST[x]
                if x == "sexo":
                    if e["sexo"] in ("Masculino","Feminino"):
                        user.sexo = e["sexo"]
                elif x == "password":
                    if len(e["password"]) > 7:
                        user.password = e["password"]
                elif x == "pr_nome":
                    if len(e["pr_nome"]) > 7:
                        user.pr_nome = e["pr_nome"]
                elif x == "ul_nome":
                    if len(e["ul_nome"]) > 7:
                        user.ul_nome = e["ul_nome"]
                elif x == "contacto":
                    if len(e["contacto"]) > 8:
                        user.contacto = e["contacto"]
                elif x == "email":
                    if len(e["email"]) > 7:
                        user.email = e["email"]
                elif x == "links":
                    if len(e["links"]) > 6:
                        user.links = e["links"]
                elif x == "sobre":
                    if len(e["sobre"]) > 10:
                        user.sobre = e["sobre"]
                elif x == "pais":
                    if len(e["pais"]) > 2:
                        user.pais = e['pais']
            if "imagem" in request.FILES:
                if len(request.FILES) > 0:
                    user.imagem = request.FILES["imagem"]
            user.save()
            return render(request,"my_info.html",{"user":user})
        else:
            return render(request,"my_info.html",{"user":user})

def ver_studios(request):
    return render(request,"lojas.html",{"download":"Baixar","musics":getranmusics(),"my_lojas":"Musicas aleatorias","my_studious":"Todos Studios de Beat-Box","bem_vindo":"Divirata-se em BeatBox","studios":studio.objects.all()})
def ver_lojas(request):
    return render(request,"lojaa.html",{"download":"Baixar","studios":loja.objects.all(),"my_lojas":"Musicas aleatorias","my_studious":"Todas lojas de Beat-Box","bem_vindo":"Divirata-se em BeatBox","musics":getranmusics()})
def ver_studio_especifico(request,slug,pk):
    user = cantor.objects.filter(slug=slug).first()
    if user == None:
        return render(request,"404.html",{"erro":"A conta que estás a tentar acessar não existe"})
    else:
        st = studio.objects.filter(slug=pk).first()
        if st == None:
            return render(request,"404.html",{"erro":"O Studio que estás a tentar acessar não existe"})
        else:
            return render(request,"studio.html",{"like":"no","studio":st,"user":user})
        
def ver_loja_especifica(request,slug,pk):
    user = cantor.objects.filter(slug=slug).first()
    if user == None:
        return render(request,"404.html",{"erro":"A conta que estás a tentar acessar não existe"})
    else:
        st = loja.objects.filter(slug=pk).first()
        if st == None:
            return render(request,"404.html",{"erro":"A loja que estás a tentar acessar não existe"})
        else:
            return render(request,"studio.html",{"like":"no","studio":st,"user":user})
def musicassss(request,slug):
    ca = cantor.objects.filter(slug=slug).first()
    if ca != None:
        if request.method == "POST":
            r = request.META.get("HTTP_ORIGIN")
            if len(request.POST["procurar"]) == 0:
                e = datad()
                e["user"] = ca
                e["musicas"] = musica.objects.all()
                e["about_blog"] = "Uma pesquisa tem de ter mais de um caratere"
                return render(request,"musics_for_users.html",e)
            else:
                r1 = []
                if " " in r:
                    for x in r.split(" "):
                        r1.append(x)
                        r1.append(str(x).capitalize())
                        r1.append(str(x).upper())
                        r1.append(str(x).lower())
                r1.append(r)
                r1.append(str(r).capitalize())
                r1.append(str(r).upper())
                r1.append(str(r).lower())
                musicas = musica.objects.filter(Q(titulo__in=r1)|Q(titulo=r)|Q(titulo__contains=r)|Q(tipo=r)|Q(tipo__in=r1)|Q(tipo__contains=r)|Q(sobre=r)|Q(sobre__in=r1)|Q(sobre__contains=r)|Q(artistas=r)|Q(artistas__in=r1)|Q(artistas__contains=r)|Q(video=r)|Q(video__in=r1)|Q(video__contains=r)|Q(audio=r)|Q(audio__in=r1)|Q(audio__contains=r)).all()
                e = datad()
                e["user"] = ca
                e["musicas"] = musicas
                return render(request,"musics_for_users.html",e)
        else:
            e = datad()
            e["user"] = ca
            e["musicas"] = musica.objects.all()
            
            return render(request,"musics_for_users.html",e)
    else:
        return render(request,"404.html",{"erro":"A conta que estás a tentar acessar não existe"})
def musicass(request,slug,pk):
    user = cantor.objects.filter(slug=slug).first()
    if user == None:
        return render(request,"404.html",{"erro":"A conta que estás a tentar acessar não existe"})
    else:
        l = musica.objects.filter(slug=pk).first()
        if l == None:
            return render(request,"404.html",{"erro":"A musica que estás a tentar acessar não existe"})
        else:
            return render(request,"musicViewUser.html",{"user":user,"music":l})

def meus_studios(request,slug):
    user = cantor.objects.filter(slug=slug).first()
    if user == None:
        return render(request,"404.html",{"erro":"A conta que estás a tentar acessar não existe"})
    else:
        return render(request,"studios.html",{"my_lojas":"Musicas do Beat-Box","my_studious":"Meus Studios","bem_vindo":"Bem-vindo a Beat-Box","title":"Meus Studios","voltar":"Ir a minha pagina ","download":"Baixar","musics":getranmusics(),"studios":studio.objects.filter(de=user.id).all(),"user":user})

def minhas_lojas(request,slug):
    user = cantor.objects.filter(slug=slug).first()
    if user == None:
        return render(request,"404.html",{"erro":"A conta que estás a tentar acessar não existe"})
    else:
        return render(request,"studios1.html",{"my_lojas":"Musicas do Beat-Box","my_studious":"Minhas lojas","bem_vindo":"Bem-vindo a Beat-Box","title":"Meus Studios","voltar":"Ir a minha pagina ","download":"Baixar","musics":getranmusics(),"studios":loja.objects.filter(de=user.id).all(),"user":user})

def seeing_especific_music(request,pr):
    music = musica.objects.filter(slug=pr).first()
    if music == None:
        return render(request,"404.html",{"erro":"A musica que estás a tentar acessar não existe"})
    else:
        return render(request,"musicView.html",{"like":"not","Pagina_inicial":"Pagina inicial","procurar":"Procurar","music":music,"origin":str(request.META.get("HTTP_HOST"))})
def seeing_especific_music_with_user(request,slug,pr):
    user = cantor.objects.filter(slug=slug).first()
    if user == None:
        return render(request,"404.html",{"erro":"A conta que estás a tentar acessar não existe"})
    else:
        music = musica.objects.filter(slug=pr).first()
        if music == None:
            return render(request,"404.html",404)
        else:
            return render(request,"musicViewUser.html",{"like":"not","user":user,"origin":str(request.META.get("HTTP_HOST")),"Pagina_inicial":"Pagina inicial","procurar":"Procurar","music":music})

def ver_studios_es(request,pk):
    st = studio.objects.filter(slug=pk).first()
    if st == None:
        return render(request,"404.html",{"erro":"O Studio que estás a tentar acessar não existe"})
    else:
        return render(request,"StView.html",{"like":"no","origin":str(request.META.get("HTTP_HOST")),"loja":st,"type":"studio","link":"Link do studio","Contacto":"Contacto","Pais":"Pais","Provincia":"Provincia","Cidade":"Cidade","Localizacao":"Localização"})
        
def ver_lojas_es(request,pk):
    st = loja.objects.filter(slug=pk).first()
    if st == None:
        return render(request,"404.html",{"erro":"A Loja que estás a tentar acessar não existe"})
    else:
        return render(request,"StView.html",{"like":"no","origin":str(request.META.get("HTTP_HOST")),"loja":st,"type":"loja","link":"Link da loja","Contacto":"Contacto","Pais":"Pais","Provincia":"Provincia","Cidade":"Cidade","Localizacao":"Localização"})
def liking_music(request,pr):
    music = musica.objects.filter(slug=pr).first()
    if music != None:
        music.gostos = int(music.gostos) + 1
        music.save()
        return render(request,"musicView.html",{"like":"yes","Pagina_inicial":"Pagina inicial","procurar":"Procurar","music":music,"origin":str(request.META.get("HTTP_HOST"))})
    else:
        return render(request,"404.html",{"error":"A musica que procura não foi encontrada"})
def blaming_music(request,pr):
    music = musica.objects.filter(slug=pr).first()
    if music == None:
        return render(request,"404.html",{"error":"A musica que procuras não foi encontrada"})
    else:
        if request.method == "POST":
            e = {}
            for x in request.POST:
                e[x] = request.POST[x]
            if len(e["sobre"]) >= 3:
                de = denuncia(para=music.id,sobre=e["sobre"],to="musica")
                music.denuncias = int(music.denuncias) + 1
                de.save()
                music.save()
                return HttpResponseRedirect(str(request.META.get("HTTP_HOST"))+"music/"+str(pr))
            else:
                return render(request,"denunciar.html",{"erro":"Adicione conteudo a denuncia para que seja valida"})
        else:
            return render(request,"denunciar.html")
def artistas_see(request):
    artistas = cantor.objects.all()
    return render(request,"artistas.html",{"artistas":artistas})
def artista_see(request,pk):
    can = cantor.objects.filter(id=pk).first()
    if can == None:
        return render(request,"404.html",{"erro":"O artista que procuras não foi achado"})
    else:
        mu = musica.objects.filter(de=can.id).all()
        return render(request,"seeArt.html",{"gosto":"not","artista":can,"musics":mu,"q":len(mu)})
def artista_g(request,pk):
    can = cantor.objects.filter(id=pk).first()
    if can != None:
        can.gostos = int(can.gostos) + 1
        can.save()
        mu = musica.objects.filter(de=can.id).all()
        return render(request,"seeArt.html",{"gosto":"yes","artista":can,"musics":mu,"q":len(mu)})
    else:
        return render(request,"404.html",{"erro":"O artista que procuras não foi achado"})
def artista_d(request,pk):
    can= cantor.objects.filter(id=pk).first()
    if can == None:
        return render(request,"404.html",{"error":"O artista que procuras não foi encontrado"})
    else:
        if request.method == "POST":
            e = {}
            for x in request.POST:
                e[x] = request.POST[x]
            if len(e["sobre"]) >= 3:
                de = denuncia(para=can.id,sobre=e["sobre"],to="cantor")
                can.denuncias = int(can.denuncias) + 1
                de.save()
                can.save()
                return HttpResponseRedirect(str(request.META.get("HTTP_HOST"))+"artistas/"+str(pk))
            else:
                return render(request,"denunciar.html",{"erro":"Adicione conteudo a denuncia para que seja valida"})
        else:
            return render(request,"denunciar.html")
def denunciar_s(request,pk):
    st = studio.objects.filter(slug=pk).first()
    if st == None:
        return render(request,"404.html",{"erro":"O Studio que procuras não foi encontrado"})
    else:
        if request.method == "POST":
            e= {}
            for x in request.POST:
                e[x] = request.POST[x]
            if len(e["sobre"]) > 2:
                de = denuncia(para=st.id,sobre=e["sobre"],to="studio")
                de.save()
                st.denuncias = int(st.denuncias) + 1
                st.save()
                return HttpResponseRedirect(str(request.META.get("HTTP_HOST"))+"studios/"+str(pk))
            else:
                 return render(request,"denunciar.html",{"erro":"Adicione conteudo a denuncia para que seja valida"})
        else:
            return render(request,"denunciar.html")
def denunciar_l(request,pk):
    st = loja.objects.filter(slug=pk).first()
    if st == None:
        return render(request,"404.html",{"erro":"A loja que procuras não foi encontrada"})
    else:
        if request.method == "POST":
            e= {}
            for x in request.POST:
                e[x] = request.POST[x]
            if len(e["sobre"]) > 2:
                de = denuncia(para=st.id,sobre=e["sobre"],to="loja")
                de.save()
                st.denuncias = int(st.denuncias) + 1
                st.save()
                return HttpResponseRedirect(str(request.META.get("HTTP_HOST"))+"lojas/"+str(pk))
            else:
                 return render(request,"denunciar.html",{"erro":"Adicione conteudo a denuncia para que seja valida"})
        else:
            return render(request,"denunciar.html")
def gostar_s(request,pk):
    st = studio.objects.filter(slug=pk).first()
    if st == None:
        return render(request,"404.html",{"erro":"O Studio que procuras não foi encontrado"})
    else:
        return render(request,"StView.html",{"like":"yes","origin":str(request.META.get("HTTP_HOST")),"loja":st,"type":"studio","link":"Link da do Studio","Contacto":"Contacto","Pais":"Pais","Provincia":"Provincia","Cidade":"Cidade","Localizacao":"Localização"})

def gostar_l(request,pk):
    st = loja.objects.filter(slug=pk).first()
    if st == None:
        return render(request,"404.html",{"erro":"A loja que procuras não foi encontrada"})
    else:
        return render(request,"StView.html",{"like":"yes","origin":str(request.META.get("HTTP_HOST")),"loja":st,"type":"loja","link":"Link da Loja","Contacto":"Contacto","Pais":"Pais","Provincia":"Provincia","Cidade":"Cidade","Localizacao":"Localização"})

def sharing(request,slug):
    can = cantor.objects.filter(slug=slug).first()
    if can == None:
        return render(request,"404.html",{"erro":"A sua conta nnão foi encontrada"})
    else:
        musicas = musica.objects.filter(de=can.id).all()
        studios = studio.objects.filter(de=can.id).all()
        lojas = loja.objects.filter(de=can.id).all()
        return render(request,"links_sha.html",{"artista":can,"lojas":lojas,"musicas":musicas,"studios":studios,"origin":str(request.META.get("HTTP_HOST"))})

def pro(r="aeiou"):
    r1 = []
    if " " in r:
        for x in r.split(" "):
            r1.append(x)
            r1.append(str(x).capitalize())
            r1.append(str(x).upper())
            r1.append(str(x).lower())
    r1.append(r)
    r1.append(str(r).capitalize())
    r1.append(str(r).upper())
    r1.append(str(r).lower())
    musicas = musica.objects.filter(Q(titulo__in=r1)|Q(titulo=r)|Q(titulo__contains=r)|Q(tipo=r)|Q(tipo__in=r1)|Q(tipo__contains=r)|Q(sobre=r)|Q(sobre__in=r1)|Q(sobre__contains=r)|Q(artistas=r)|Q(artistas__in=r1)|Q(artistas__contains=r)|Q(video=r)|Q(video__in=r1)|Q(video__contains=r)).all()
    st = studio.objects.filter(Q(localizacao__in=r1)|Q(localizacao=r)|Q(localizacao__contains=r)|Q(pais=r)|Q(pais__in=r1)|Q(pais__contains=r)|Q(nome=r)|Q(nome__in=r1)|Q(nome__contains=r)|Q(cidade=r)|Q(cidade__in=r1)|Q(cidade__contains=r)|Q(provincia=r)|Q(provincia__contains=r)|Q(provincia__in=r1)).all()
    lj = loja.objects.filter(Q(localizacao__in=r1)|Q(localizacao=r)|Q(localizacao__contains=r)|Q(pais=r)|Q(pais__in=r1)|Q(pais__contains=r)|Q(nome=r)|Q(nome__in=r1)|Q(nome__contains=r)|Q(cidade=r)|Q(cidade__in=r1)|Q(cidade__contains=r)|Q(provincia=r)|Q(provincia__contains=r)|Q(provincia__in=r1)).all()
    cn = cantor.objects.filter(Q(pr_nome__in=r1)|Q(ul_nome__in=r1)|Q(pr_nome=r)|Q(pr_nome__contains=r)|Q(ul_nome=r)|Q(ul_nome__contains=r)).all()
    return {"artistas":cn,"musicas":musicas,"lojas":lj,"studios":st}

def pro_st(request,r):
    e = pro(r=r)
    f= {"download":"Baixar","musics":getranmusics(),"my_lojas":"Musicas aleatorias","my_studious":"Todos Studios de Beat-Box","bem_vindo":"Divirata-se em BeatBox","studios":studio.objects.all()}
    for x in e:
        f[x] = e[x]
    return render(request,"lojas.html",f)
def pro_lj(request,r):
    e = pro(r=r)
    f = {"download":"Baixar","studios":e["lojas"],"my_lojas":"Musicas aleatorias","my_studious":"Todas lojas de Beat-Box","bem_vindo":"Divirata-se em BeatBox","musics":getranmusics()}
    for x in e:
        f[x] = e[x]
    f["studios"] = e["lojas"]
    return render(request,"lojaa.html",f)
def pro_ar(request,r):
    e = pro(r=r)
    return render(request,"artistas.html",{"artistas":e["artistas"]})
def termos(request):
    return render(request,"terms.html",{"terms":terms.objects.all(),"tema":"Os nossos termos e condições","nH":"Nenhum termo ou condição"})
def sair(request,slug):
    ca = get_object_or_404(cantor,slug=str(slug))
    c = redirect('/myaccount/')
    c.delete_cookie("boxcookie")
    return c
