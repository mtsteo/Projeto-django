from django.shortcuts import render, redirect
from .models import jogos, administradores
from .forms import jogoForm, AdminForm
from datetime import date


def home(request):
    jogoDoDia=[]
    data_atual = date.today()

    partidas = jogos.objects.all()
    for partida in partidas:
        if partida.data == data_atual:
            jogoDoDia.append(partida)
    
    
    return render(request, 'home/home.html', {'data_atual': data_atual , 'jogos': jogoDoDia})


def emp(request):
    if request.method == "POST":
        form = jogoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = jogoForm()
    return render(request, 'administrador/index.html', {'form': form})


def admin(request):

    return render(request, 'administrador/login.html')


def login(request):
    if request.method == "POST":
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        


        
        try:
            if administradores.objects.filter(usuario=usuario, senha=senha).exists():
                return render(request, 'administrador/show.html')
            else:

             return render(request,'administrador/login.html')

        # Se o usuário existir, faça algo aqui
        except:
             return render(request,'administrador/login.html')
        # Se o usuário não existir, faça algo aqui


def show(request):
    partidas = jogos.objects.all()
    return render(request, "administrador/show.html", {'jogos': partidas})


def edit(request, id):
    partidas = jogos.objects.get(id=id)
    return render(request, 'administrador/edit.html', {'jogos': partidas})


def update(request, id):
    partidas = jogos.objects.get(id=id)

    form = jogoForm(request.POST, instance=partidas)

    if form.is_valid():
        form.save()
        return redirect("/show")
    else:
        print("Formulário inválido:", form.errors)
    return render(request, 'administrador/edit.html', {'jogos': partidas})


def destroy(request, id):
    jogo = jogos.objects.get(id=id)
    jogo.delete()
    return redirect("/show")
