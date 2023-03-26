from django.forms import ModelForm
from .models import Posts, Tag, Categoria

class PostsForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['titulo', 'contenido', 'pais', 'tag', 'categoria']

class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['nombre', 'descripcion']

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']