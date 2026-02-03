from django.shortcuts import render

# Create your views here.
# Vista para la página principal del catálogo
def index(request):
    return render(request, 'catalogo/index.html')