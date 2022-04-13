from django.urls import path
from .views import index, clases, confirmacion, horarioAtencion, plan, quienSomos, basededatos, crearUsuario, form_mod_usuario, form_del_usuario 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path ('', index, name = "index"), #con este metodo se llama a la pagina index como primer opcion para mirar
    path ('clases', clases, name = "clases"),
    path ('confirmacion', confirmacion, name = "confirmacion"),
    path ('horarioAtencion', horarioAtencion, name = "horarioAtencion"),
    path ('plan', plan, name = "plan"),
    path ('quienSomos', quienSomos, name = "quienSomos"),
    path ('basededatos', basededatos, name = "basededatos"),
    path ('crearUsuario/', crearUsuario, name = "crearUsuario"),
    path ('form_mod_usuario/<id>', form_mod_usuario, name = "form_mod_usuario"), #el <id> corresponde a la primary key que se esta mandando en el html
    path ('form_del_usuario/<id>', form_del_usuario, name = "form_del_usuario"), 
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)