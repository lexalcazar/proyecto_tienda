from django.urls import path
from catalogo.views import index


urlpatterns = [
    # pagina de inicio del catalogo
    path('', index, name='index'),
    
]
