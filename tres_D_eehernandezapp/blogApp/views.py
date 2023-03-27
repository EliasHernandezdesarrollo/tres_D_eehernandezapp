from django.shortcuts import render, redirect
from blogApp.models import Pais, Posts, Categoria, Tag
from django.utils import timezone
from .forms import PostsForm, TagForm, CategoriaForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index_page(request):
    return render(request, 'index_page.html')
@login_required
def home(request):
    if request.user.is_authenticated:
        posts = Posts.objects.all()
        return render(request, 'home.html', {"posts": posts})
    else:
        return redirect("/login/")

@login_required
def posts(request):
    if request.user.is_authenticated:
        try:
            user = request.user
            posts = Posts.objects.filter(user=user)
            return render(request, 'posts.html', {"posts": posts})
        except Posts.DoesNotExist:
            return render(request, 'posts.html')
    else:
        return redirect("/login/")

@login_required
def create_post(request):
    user = request.user
    if user.is_authenticated:
        if request.method == 'POST':
            form = PostsForm(request.POST)
            if form.is_valid():
                new_post = form.save(commit=False)
                new_post.user = request.user
                new_post.actualizo_el = timezone.now()
                new_post.save()
                return redirect('/posts/')
        else:
            return render(request, 'create_post.html', {"form": PostsForm })
    else:
        return redirect("/login/")


@login_required
def create_tag(request):
    user = request.user
    if user.is_authenticated:
        if request.method == 'POST':
            nombre_old = request.POST.get('nombre')
            if Tag.objects.filter(nombre=nombre_old).exists():
                return render(request, 'create_tag.html', {"form": TagForm, "message": "Este Tag Ha Existe!"})
            form = TagForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/posts/')
        else:
            return render(request, 'create_tag.html', {"form": TagForm})
    else:
        return redirect("/login/")


@login_required
def create_categoria(request):
    user = request.user
    if user.is_authenticated:
        if request.method == 'POST':
            categoria_formulario = request.POST.get('nombre')
            if Categoria.objects.filter(nombre=categoria_formulario).exists():
                return render(request, 'create_tag.html', {"form": TagForm, "message": "Este Tag Ha Existe!"})
            form = CategoriaForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/posts/')
        else:
            return render(request, 'create_categoria.html', {"form": CategoriaForm})
    else:
        return redirect("/login/")


@login_required
def edit_post(request, id):
    user = request.user
    if user.is_authenticated:
        if request.method != 'POST':
            post = Posts.objects.get(id=id)
            form = PostsForm(instance=post)
            return render(request, 'edit_post.html', {"form": form})
        else:
            post = Posts.objects.get(id=id)
            form = PostsForm(request.POST, instance=post)
            form.save()
            return redirect("/posts/")
    else:
        return redirect("/login/")


@login_required
def delete_post(request, id):
    user = request.user
    if user.is_authenticated:
        post = Posts.objects.get(id=id)
        print(post)
        post.delete()
        return redirect("/posts/")
    else:
        return redirect("/login/")


@login_required
def search(request):
    user = request.user
    if user.is_authenticated:
        if request.method == "POST":
            busqueda = request.POST.get('busqueda')
            posts = Posts.objects.filter(contenido__contains=busqueda)
            return render(request, 'search.html', {"busqueda": busqueda, "posts": posts})
        else:
            return redirect("/posts/")
    else:
        return redirect("/login/")


