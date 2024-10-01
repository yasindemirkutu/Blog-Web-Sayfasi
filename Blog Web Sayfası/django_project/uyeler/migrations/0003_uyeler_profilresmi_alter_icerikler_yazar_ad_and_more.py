# Generated by Django 4.2.7 on 2023-12-11 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uyeler', '0002_icerikler'),
    ]

    operations = [
        migrations.AddField(
            model_name='uyeler',
            name='profilresmi',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='icerikler',
            name='yazar_ad',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='icerikler',
            name='yazar_kullaniciAdi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='icerikler', to='uyeler.uyeler'),
        ),
    ]
