from django.shortcuts import render
from inicio.forms import CrearAlumnoFormulario
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