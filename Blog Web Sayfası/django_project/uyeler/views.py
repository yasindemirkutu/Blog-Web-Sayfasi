from django.shortcuts import render
from django.http import HttpResponse
from .models import Uyeler,Icerikler
from django.template import loader
import datetime
from django.views.decorators.csrf import csrf_exempt #ÖNEMLİ
from django.core.files.storage import FileSystemStorage

def hakkimizda(request):
    if request.method == 'POST':
        data = request.POST['uyeSil']
        print('aaaaa')
        print(data)
        Uyeler.objects.get(id=data).delete()
    uyelistesi = Uyeler.objects.all().values()
    sablon = loader.get_template('hakkimizda.html')
    veriler = {
      'uyelistesi' : uyelistesi
    }

    return HttpResponse(sablon.render(veriler,request))

def icerikler(request):
    if request.method == 'POST':
        data = request.POST['uyeSil']
        print('aaaaa')
        print(data)
        Uyeler.objects.get(id=data).delete()
    uyelistesi = Uyeler.objects.all().values()
    sablon = loader.get_template('icerikler.html')
    veriler = {
      'uyelistesi' : uyelistesi
    }

    return HttpResponse(sablon.render(veriler,request))


def yeniuye(request):
    sablon = loader.get_template('yeni.html')
    return HttpResponse(sablon.render())

def uyedetay(request, uyeno): # view fonksiyonumuz
 return HttpResponse(str(uyeno) + " nolu üyenin detay sayfası")

def uyesayfasi(request):
 uyelistesi = Uyeler.objects.all().values()
 sablon = loader.get_template('liste.html')
 veriler = {
 'uyelistesi': uyelistesi
 }
 return HttpResponse(sablon.render(veriler, request))
@csrf_exempt
def yeniuye(request):
 hatalar = []
 bilgi = {'yeniKayit': "False", 'hatalistesi': hatalar}
 if request.method == 'POST':
        adi = request.POST['adi']
        if len(adi) < 2:
            hatalar.append("İsim 2 karakterden küçük olamaz")
        soyadi = request.POST['soyadi']
        
        if len(soyadi) < 2:
            hatalar.append("Soyisim 2 karakterden küçük olamaz")
        kullaniciAdi = request.POST['kullaniciAdi']

        if len(kullaniciAdi) < 5:
            hatalar.append("Kullanıcı Adı 5 karakterden küçük olamaz")
        uyeno = request.POST['uyeno']

        if len(uyeno) < 3:
            hatalar.append("Üye numarası 3 haneden küçük olamaz")
        cinsiyet = request.POST['cinsiyet']
        
        profilResmi = request.FILES.get('profil', False)
        print(profilResmi.name)
        if profilResmi != False:
            if profilResmi.name.split(".")[-1] in ['jpg', 'png']:
                fs = FileSystemStorage()
                yukle = fs.save('images/' + profilResmi.name, profilResmi)
                profilResmi_url = fs.url(yukle)
            else:
                hatalar.append("Sadece jpg veya png uzantılı resim yüklenebilir!")
        else:
            hatalar.append("Profil resmi boş olamaz!")
        
        
        cv = request.FILES.get('cv', False)
        if cv != False:
            if cv.name.split(".")[-1] in ['pdf']:
                fs = FileSystemStorage()
                yukle = fs.save('cvler/' + cv.name, cv)
                cv_url = fs.url(yukle)
            else:
                hatalar.append("Sadece pdf  uzantılı CV yükleyebilirsiniz. ")
        else:
            hatalar.append("CV dosyası boş olamaz.")


        if len(hatalar) == 0:
            yeniUye = Uyeler(ad=adi, soyad=soyadi,profilresmi = profilResmi_url,cv = cv_url, uyeno=uyeno, kullaniciAdi=kullaniciAdi, cinsiyet=cinsiyet)
            yeniUye.save()
            bilgi['yeniKayit'] = "True" 
        else:
            bilgi['hatalistesi'] = hatalar


 sablon2 = loader.get_template('yeni.html')
 return HttpResponse(sablon2.render(bilgi, request))


 
def uyedetay (request, uyeid):
    bilgi = {'uye' : Uyeler.objects.get(id = uyeid)}
    sablon = loader.get_template('detay.html')
    return HttpResponse(sablon.render(bilgi,request))

def uyeduzenle (request, uyeid):
    bilgi = {'uye' : Uyeler.objects.get(id = uyeid)}
    sablon = loader.get_template('duzenle.html')
    return HttpResponse(sablon.render(bilgi ,request))

def uyeduzenle(request, uyeid):
    bilgi = {'uye':Uyeler.objects.get(id = uyeid),
              'guncellendimi': "False"}

    if request.method == 'POST':
        print("ffff")
        uye = Uyeler.objects.get(id = uyeid)
        uye.ad = request.POST['adi']
        uye.soyad = request.POST['soyadi']
        uye.uyeno = request.POST['uyeno']
        uye.kullaniciAdi = request.POST['kullaniciAdi']
        uye.cinsiyet = request.POST['cinsiyet']
     
        uye.save()
        bilgi['uye'] = uye
        bilgi['guncellendimi'] = "True"
    sablon = loader.get_template('duzenle.html')
    return HttpResponse(sablon.render(bilgi, request))
