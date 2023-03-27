from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from .models import Usuario
from blogApp.models import Pais

# Create your views here.
def login_app(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        print(email, password)
        try:
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('/home/')
            else:
                return render(request, 'registration/login.html', {"message": "Correo o constrasena incorrecto. Ingresa de nuevo."})
        except Usuario.DoesNotExist:
            return render(request, 'registration/login.html', {"message": "El usuario ingresado no existe."})

    else:
        return render(request, 'registration/login.html')

def register(request):
    if request.method != 'POST':
        paises = Pais.objects.all()
        return render(request, 'register.html', {"paises": paises})
    else:
        if request.POST["password"] == request.POST["password2"]:
            email = request.POST["email"]
            password = request.POST["password"]
            pais_pk = request.POST["pais"]
            cedula = request.POST["cedula"]
            nombres = request.POST["nombres"]
            # try:
            pais = Pais.objects.get(id=pais_pk)
            Usuario.objects.create_user(email=email, password=password, cedula=cedula, nombres=nombres)
            return redirect('/login/')
            # except:
                # paises = Pais.objects.all()
                # return render(request, 'register.html', {"paises": paises, "message": "Ocurrio un error, intenta de nuevo."})
        else:
            paises = Pais.objects.all()
            return render(request, 'register.html', {"paises": paises, "message": "Las constrasenas no son iguales."})

def exit(request):
    logout(request)
    return redirect('/login/')