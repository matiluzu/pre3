from django.shortcuts import render
from inicio.forms import CrearAlumnoFormulario, BuscarAlumnoFormulario 
from inicio.models import Alumno

# Create your views here.

def inicio(request):
    return render(request, 'inicio/inicio.html')

def crear_alumno(request):
    mensaje = ''    
    if request.method == "POST":
        formulario = CrearAlumnoFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            alumno = Alumno(nombre = info['nombre'],apellido = info['apellido'], edad=info['edad'], dni=info['dni'])
            alumno.save()
            mensaje = f'Se dio de alta a {alumno.nombre} como alumno'
        else:
            return render(request, 'inicio/crear_alumno.html', {'formulario' : formulario})
                    
    formulario = CrearAlumnoFormulario()
    return render(request, 'inicio/crear_alumno.html', {'formulario' : formulario, 'mensaje':mensaje})

def listar_alumnos(request):
    formulario = BuscarAlumnoFormulario(request.GET)
    listado = []
    if formulario.is_valid():
        busqueda = formulario.cleaned_data["dni"]
        listado = Alumno.objects.filter(dni=busqueda)
    else:
        print("DNI Not Found")
    
    return render(request, 'inicio/listar_alumnos.html',{'formulario':formulario, "alumnos":listado})