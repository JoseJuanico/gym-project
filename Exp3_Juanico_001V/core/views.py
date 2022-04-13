from django.shortcuts import redirect, render
from .models import Tipo, Usuario
from .forms import UsuarioForm


# Create your views here.

def index (request):
    
    return render (request, 'index.html')

def clases (request):
    return render (request, 'clases.html')

def confirmacion (request):
    return render (request, 'confirmacion.html')

def horarioAtencion (request):
    return render (request, 'horarioAtencion.html')

def plan (request):
    return render (request, 'plan.html')

def quienSomos (request):
    return render (request, 'quienSomos.html')

def basededatos(request):
    usuario = Usuario.objects.all() #acceso a los usuarios ya creados por admin
    return render (request, 'core/basededatos.html', context = {'datos': usuario})


def crearUsuario(request):
    if request.method == 'POST':
        usuario = UsuarioForm(request.POST)
        if usuario.is_valid(): #esta checkenado los parametros del objeto, si son correctos
            usuario.save()  #metodo que crea un nuevo objeto, reemplaza al metodo insert de bd
            return redirect('index') #luego de almacenarlo redireccionme al index
    else:
        usuario = UsuarioForm() #en este caso se asigna un objeto vacio
    return render(request, 'core/form_crearusuario.html', {'usuario': usuario}) #y se debe enviar al formulario en este caso
    #de esta forma se controla el ingreso


def form_mod_usuario(request, id): #se recibe el id aparte
    usuario = Usuario.objects.get(rut = id) #el rut qeu se recibe por parametro, lo recibe para ir a buscar el objeto al admin de djando

    datos = {
        'form': UsuarioForm(instance = usuario) #form toma el valor del form de UsuarioForm, la planilla creada
    }
    if request.method == 'POST': 
        formulario = UsuarioForm(data = request.POST, instance = usuario) #se crea nuevo objeto
        if formulario.is_valid:
            formulario.save() #permite guardar el objeto ya modificado
            return redirect('basededatos')
    return render (request, 'core/form_mod_usuario.html', datos)
    
def form_del_usuario(request, id):
    usuario = Usuario.objects.get(rut = id)
    usuario.delete()
    return redirect('basededatos')
  