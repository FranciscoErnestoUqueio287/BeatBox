from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *
from db_file_storage import views
urlpatterns = [
    path("terms/",termos,name="terms"),
    path("myaccount/<str:slug>/sha/",sharing,name="compartilhar"),
    path("",mainpage,name="Pagina_inicial"),
    path("ajuda/<pr>/",helping_in,name="Ajuda"),
    path("ajuda/",helping,name="Ayuda"),
    path("myaccount/<str:slug>/sair/",sair,name="Sair"),
    path("myaccount/<str:slug>/loja/<str:pk>/",minha_loja,name="Minha_loja"),
    path("myaccount/<str:slug>/studio/<str:pk>/",meu_studio,name="Meu_studio"),
    path("myaccount/<str:slug>/my_stores/",minhas_lojas,name="Minhas_lojas"),
    path("myaccount/<str:slug>/my_studios/",meus_studios,name="Meus_estudios"),
    path("myaccount/<str:slug>/",singerin,name="user_in"),
    path("myaccount/<str:slug>/my_musics/<str:pk>/",user_musica,name="ver_musica"),
    path("myaccount/<str:slug>/post/undefined/<str:pk>/",user_musica,name="ver_musica2"),
    path("myaccount/<str:slug>/musics/<str:pr>/",seeing_especific_music_with_user,name="Ver_a_musica"),
    path("myaccount/<str:slug>/my_musics/",user_musicas,name="user_in_musicas"),
    path("criar_conta/",criarcantor,name="cria_"),
    path("music/<pr>",seeing_especific_music,name="Vendo_musica_especifica"),
    path("music/<pr>/gostar/",liking_music,name="liking_music"),
    path("music/<pr>/denunciar/",blaming_music,name="blaming_music"),
    path("procura=<str:r>/",promus,name="Procura_de_musica"),
    path("procura_st=<str:r>/",pro_st,name="Procura_de_studio"),
    path("procura_lj=<str:r>/",pro_lj,name="Procura_de_loja"),
    path("procura_ar=<str:r>/",pro_ar,name="Procura_de_artista"),
    path("myaccount/",userlog,name="minha_conta"),
    path("artistas/",artistas_see,name="artistas_see"),
    path("artistas/<pk>/",artista_see,name="artista_see"),
    path("artistas/<pk>/gostar/",artista_g,name="artista_g"),
    path("artistas/<pk>/denunciar/",artista_d,name="artista_d"),
    path("myaccount/<str:slug>/post/",post_music,name="publicar_uma_musica"),
    path("myaccount/<str:slug>/loja/",criar_loja,name="criar_loja"),
    path("myaccount/<str:slug>/studio/",criar_studio,name="criar_studio"),
    path("myaccount/<str:slug>/my_info/",my_info_see,name="minha_info"),
    path("studios/",ver_studios,name="Ver_todos_studios"),
    path("lojas/",ver_lojas,name="Ver_todas_lojas"),
    path("studios/<pk>/",ver_studios_es,name="Ver_ess"),
    path("lojas/<pk>/",ver_lojas_es,name="Ver_esl"),
    path("studios/<pk>/denunciar/",denunciar_s,name="denunciar_s"),
    path("lojas/<pk>/denunciar/",denunciar_l,name="denunciar_l"),
    path("studios/<pk>/gostar/",gostar_s,name="gostar_s"),
    path("lojas/<pk>/gostar/",gostar_l,name="gostar_l"),
    path("myaccount/<str:slug>/studios/<str:pk>",ver_studio_especifico,name="Ver_todos_studios"),
    path("myaccount/<str:slug>/lojas/<str:pk>",ver_loja_especifica,name="Ver_todas_lojas"),
    path("filedonwloadinginBeatBoxBlogNow/",views.get_file,{"add_attachment_headers":True,"extra_headers":{"Content-Language":"pt"}},name="down"),
    path("fileSeeinginBeatBoxBlogNow/",views.get_file,{"add_attachment_headers":False,"extra_headers":{"Content-Language":"pt"}},name="see"),] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
