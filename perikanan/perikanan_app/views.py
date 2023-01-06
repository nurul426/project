from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.core import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def lokasi(request):
      tempat = Lokasi.objects.all()
      titik_json = serializers.serialize('json', tempat)
      tpi = {
          "Judul"   : "Lokasi Sebaran",
          'tempat' : tempat,
          'titik_json' : titik_json,
      }
      return render(request, "lokasi.html", tpi)

@login_required(login_url='login')
def tambahlokasi(request):
      if request.POST:
          form = FormLokasi(request.POST, request.FILES)
          if form.is_valid():
              form.save()
              form = FormLokasi()
              tempat = Lokasi.objects.all()
              tpi = {
                  "Judul"   : "Tambah Data",
                 'Title' : "Tambah Data Baru",
                 'tempat' : tempat,
                 'form'    : form,
                 'pesan'   : "Data berhasil ditambahkan"
              }
              return render(request, "tambahlokasi.html", tpi)
      else:
          form  = FormLokasi()
          tempat = Lokasi.objects.all()
          tpi = {
             "Judul"   : "Tambah Data",
             'Title'   : "Tambah Data Baru",
             'tempat' : tempat,
             'form'    : form,
          }
          return render(request, "tambahlokasi.html", tpi)

@login_required(login_url='login')
def editlokasi(request, id):
      tempat = Lokasi.objects.get(pk=id)
      if request.POST:
          form = FormLokasi(request.POST, request.FILES, instance=tempat)
          if form.is_valid():
              form.save()
              tpi = {
                  "Judul"   : "Edit Data",
                  'Title' : "Edit Data",
                  'tempat' : tempat,
                  'form'  : form,
                  'pesan' : "Data berhasil diubah"
              }
              return render(request, "editlokasi.html", tpi)
      else:
          form = FormLokasi(instance=tempat)
          tpi = {
          "Judul"   : "Edit Data",
          'Title' : "Edit Data",
          'tempat' : tempat,
          'form'  : form,
           }
      return render(request, "editlokasi.html", tpi)

@login_required(login_url='login')
def hapuslokasi(request, id):
    tempat = Lokasi.objects.get(pk=id)
    tempat.delete()
    
    return redirect("/lokasi/")

@login_required(login_url='login')
def produksi(request):
      jumlah = Produksi.objects.all()
      tpi = {
          "Judul"   : "Biota",
          'jumlah' : jumlah,
      }
      return render(request, "produksi.html", tpi)

@login_required(login_url='login')
def tambahproduksi(request):
      if request.POST:
          form = FormProduksi(request.POST)
          if form.is_valid():
              form.save()
              form = FormProduksi()
              jumlah = Produksi.objects.all()
              tpi = {
                  "Judul"   : "Tambah Data",
                 'Title' : "Tambah Data Baru",
                 'jumlah' : jumlah,
                 'form'    : form,
                 'pesan'   : "Data berhasil ditambahkan"
              }
              return render(request, "tambahproduksi.html", tpi)
      else:
          form  = FormProduksi()
          jumlah = Produksi.objects.all()
          tpi = {
             "Judul"   : "Tambah Data",
             'Title'   : "Tambah Data Baru",
             'jumlah' : jumlah,
             'form'    : form,
          }
          return render(request, "tambahproduksi.html", tpi)

@login_required(login_url='login')
def editproduksi(request, id):
      jumlah = Produksi.objects.get(pk=id)
      if request.POST:
          form = FormProduksi(request.POST, instance=jumlah)
          if form.is_valid():
              form.save()
              tpi = {
                  "Judul"   : "Edit Data",
                  'Title' : "Edit Data",
                  'jumlah' : jumlah,
                  'form'  : form,
                  'pesan' : "Data berhasil diubah"
              }
              return render(request, "editproduksi.html", tpi)
      else:
          form = FormProduksi(instance=jumlah)
          tpi = {
          "Judul"   : "Edit Data",
          'Title' : "Edit Data",
          'jumlah' : jumlah,
          'form'  : form,
           }
      return render(request, "editproduksi.html", tpi)

@login_required(login_url='login')
def hapusproduksi(request, id):
    jumlah = Produksi.objects.get(pk=id)
    jumlah.delete()
    
    return redirect("/produksi/")

def Pagelogin(request):
    if request.user.is_authenticated:
        return redirect ("/lokasi/")
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            pass1=request.POST.get('pass')
            user=authenticate(request, username=username, password=pass1)
            if user is not None:
                login(request, user)
                return redirect('/lokasi/')
            
        return render(request, "login.html")

def Pagesignup(request):
    if request.user.is_authenticated:
        return redirect ("/lokasi/")
    else:
        if request.method=='POST':
            uname=request.POST.get('username')
            email=request.POST.get('email')
            pass1=request.POST.get('password1')
            pass2=request.POST.get('password2')
            my_user=User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('/login/')

        return render(request, "signup.html")

def Pagelogout(request):
    logout(request)
    return redirect('/login/')