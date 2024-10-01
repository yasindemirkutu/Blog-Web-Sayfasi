from django.urls import path
from . import views
urlpatterns = [
 path('yeniuye', views.yeniuye),
 path('', views.hakkimizda),
 path('detay/<int:uyeid>',views.uyedetay),
 path('duzenle/<int:uyeid>',views.uyeduzenle), 
]
