from django.contrib import admin
from .models import Uyeler, Icerikler
# Register your models here.

class UyelerAdmin(admin.ModelAdmin):
    list_display = ("uyeno", "ad", "soyad")

admin.site.register(Uyeler, UyelerAdmin)
admin.site.register(Icerikler)
