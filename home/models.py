from django.db import models

class Galeri(models.Model):
    resim = models.ImageField(upload_to='media')
    kategori = models.CharField(max_length=100)
    def __str__(self):
        return self.kategori 


class Sliders(models.Model):
    resim = models.ImageField(upload_to='media')
    baslik = models.TextField(max_length=100)
    aciklama = models.TextField(max_length=1000)
    link = models.CharField(max_length=100)
    def __str__(self):
        return self.baslik 


class Proje(models.Model):
    resim = models.ImageField(upload_to='media')
    baslik = models.TextField(max_length=200)
    aciklama = models.TextField(max_length=1000)
    def __str__(self):
        return self.baslik 

class Yonetim(models.Model):
    isim = models.TextField(max_length=100)
    unvan = models.TextField(max_length=100)
    def __str__(self):
        return self.isim

class Idare(models.Model):
    isim = models.TextField(max_length=100)
    unvan = models.TextField(max_length=100)
    def __str__(self):
        return self.isim 
    
class SastisDevam(models.Model):
    resim = models.ImageField(upload_to='media')
    baslik = models.TextField(max_length=200)
    aciklama = models.TextField(max_length=1000)
    def __str__(self):
        return self.baslik