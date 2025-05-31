from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from .models import Receta
from .forms import RecetaForm, BusquedaForm

def listar_recetas(request):
    recetas = Receta.objects.all().order_by('-fecha_publicacion')
    return render(request, 'recetas/lista.html', {'recetas': recetas})

def mostrar_receta(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    return render(request, 'recetas/detalle.html', {'receta': receta})

@login_required
def agregar_receta(request):
    if request.method == 'POST':
        form = RecetaForm(request.POST, request.FILES)
        if form.is_valid():
            receta = form.save(commit=False)
            receta.autor = request.user
            receta.save()
            return redirect('mostrar_receta', pk=receta.pk)
    else:
        form = RecetaForm()
    
    return render(request, 'recetas/form.html', {'form': form})

def buscar_recetas(request):
    if request.method == 'GET':
        form = BusquedaForm(request.GET)
        if form.is_valid():
            consulta = form.cleaned_data['query']
            recetas = Receta.objects.filter(titulo__icontains=consulta)
            return render(request, 'recetas/lista.html', {
                'recetas': recetas,
                'busqueda': consulta
            })
    else:
        form = BusquedaForm()
    
    return render(request, 'recetas/busqueda.html', {'form': form})

def listar_recetas_por_categoria(request, categoria):
    # categoria = get_object_or_404(Categoria, tipo=tipo)
    recetas = Receta.objects.filter(categoria=categoria)
    return render(request, 'recetas/lista.html', {
        'recetas': recetas,
        'categoria': categoria
    })

def registrar_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('listar_recetas')
    else:
        form = UserCreationForm()
    return render(request, 'recetas/form_usuario.html', {'form': form})