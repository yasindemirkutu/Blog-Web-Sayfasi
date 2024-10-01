from django.db import models

# Create your models here.

class Uyeler(models.Model):
    uyeno= models.IntegerField()
    ad = models.CharField(max_length=50) 
    soyad = models.CharField(max_length=50)
    kullaniciAdi = models.CharField(max_length=25)
    profilresmi = models.CharField(max_length=100, default="")
    cv = models.CharField(max_length=100, default="")
    cinsiyet = models.CharField(max_length=5)

class Icerikler(models.Model):
    yazar_kullaniciAdi = models.ForeignKey(Uyeler, on_delete=models.CASCADE,related_name='icerikler')
    yazar_ad = models.CharField(max_length=50)
    yazar_soyad = models.CharField(max_length=50)
    yazar_cinsiyet = models.CharField(max_length=5)
    icerik_ismi = models.CharField(max_length=50)
   
    

    def __str__(self):
        return f"{self.ad} {self.soyad}"
