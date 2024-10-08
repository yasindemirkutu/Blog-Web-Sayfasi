from django.http import HttpResponse
from django.template import loader
from uyeler.models import Uyeler
from django.template import loader 
from django.shortcuts import redirect # ÖNEMLİ
from django.contrib.auth import authenticate, login, logout # ÖNEMLİ
from django.contrib.auth.forms import UserCreationForm # ÖNEMLİ

def anasayfa(request):
 sablon = loader.get_template('index.html')
 return HttpResponse(sablon.render(request=request))


def user_login(request):
    bilgi = {}
    if request.method == 'POST':
        kullaniciadi = request.POST['username']
        sifre = request.POST['password']
        kullanici = authenticate(request, username=kullaniciadi, password=sifre)
        
        if kullanici is not None:
            login(request, kullanici)
            return redirect("anasayfa")
        else:
            bilgi['login'] = 'Hata'
        if request.user.is_authenticated :
            return redirect("anasayfa") 
            
    sablon = loader.get_template('login.html')
    return HttpResponse(sablon.render(bilgi, request))

def user_register(request):
    sablon = loader.get_template('register.html')
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            kullaniciadi = form.cleaned_data["username"]
            sifre = form.cleaned_data["password1"]
            kullanici = authenticate(request, username=kullaniciadi,password=sifre)
            login(request, kullanici)
            return redirect("anasayfa")
        else:
            bilgi = {"form" : form}
            return HttpResponse(sablon.render(bilgi, request))
    form = UserCreationForm()
    bilgi = {"form": form}
    return HttpResponse(sablon.render(bilgi, request))


def user_logout(request):
    logout(request)
    return redirect("anasayfa")
