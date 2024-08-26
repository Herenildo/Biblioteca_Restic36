from posixpath import basename
from django.contrib import admin
from django.urls import path, include
from core.views import CategoriaViewSet, AutorViewSet, ListaLivroAutor, ListaLivroCategoria, LivroViewSet
from rest_framework import routers

router=routers.DefaultRouter()
router.register('categoria',CategoriaViewSet, basename='Categoria')
router.register('autor',AutorViewSet, basename='Autor')
router.register('livro',LivroViewSet, basename='Livro')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('categoria/<int:pk>/livros/', ListaLivroCategoria.as_view(), name='categoria-livros'),
    path('autor/<int:pk>/livros/',ListaLivroAutor.as_view()),
]
