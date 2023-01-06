from django.db import models

# Create your models here.

class Lokasi(models.Model):
     nama_TPI  = models.CharField(max_length=100)
     g_lintang = models.FloatField(null=True)
     g_bujur = models.FloatField(null=True)
     gambar     = models.ImageField(null=True, blank=True, upload_to="images/")

     def __str__(self):
         return self.nama_TPI

class Produksi(models.Model):
     nama_ikan  = models.CharField(max_length=75)
     tahun1  = models.CharField(max_length=75)
     tahun2  = models.CharField(max_length=75)
     analisis  = models.CharField(max_length=550)
     
     def __str__(self):
         return self.nama_ikan