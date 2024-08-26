from django import views
from core import serializers
from rest_framework.response import Response
from rest_framework import status,viewsets,generics
from core import serializers
from .models import Categoria, Autor, Livro
from .serializers import CategoriaSerializer, AutorSerializer, LivroSerializer,ListaLivrosCategoriaSerializer,ListaLivrosAutorSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    """Exibindo todas as categorias"""
    queryset=Categoria.objects.all()
    serializer_class=CategoriaSerializer

class AutorViewSet(viewsets.ModelViewSet):
    """Exibindo todas os altores"""
    queryset=Autor.objects.all()
    serializer_class=AutorSerializer

class LivroViewSet(viewsets.ModelViewSet):
    """Exibindo todos os livros"""
    queryset=Livro.objects.all()
    serializer_class=LivroSerializer



class ListaLivroCategoria(generics.ListAPIView):
    """Listando os livros por categoria"""
    def get_queryset(self):
        queryset=Livro.objects.filter(categoria_id=self.kwargs['pk'])
        return queryset
    serializer_class=ListaLivrosCategoriaSerializer

class ListaLivroAutor(generics.ListAPIView):
    """Listando Livros por Autor"""
    def get_queryset(self):
        queryset=Livro.objects.filter(autor_id=self.kwargs['pk'])
        return queryset
    serializer_class=ListaLivrosAutorSerializer






