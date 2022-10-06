import json
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from wishlist.models import BarangWishlist
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
@login_required(login_url='/wishlist/login/')
def show_wishlist(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    context = {
        'list_barang': data_barang_wishlist,
        'nama': 'Sayyid Hafidzurrahman Atstsaqofi',
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "wishlist.html", context)

@login_required(login_url='/wishlist/login/')
def ajax_views(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    context = {
        'list_barang': data_barang_wishlist,
        'nama': 'Sayyid Hafidzurrahman Atstsaqofi',
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, 'wishlist_ajax.html', context)

def add_wish(request):
    if request.method == "POST":
        data = json.loads(request.POST['data'])

        new_task = BarangWishlist(nama_barang=data["nama_barang"], harga_barang=data["harga_barang"], deskripsi=data["deskripsi"])
        new_task.save()

        return HttpResponse(serializers.serialize("json", [new_task]), content_type="application/json")

    return redirect('wishlist:show_wishlist_ajax')

def parameter(request):
    data = BarangWishlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def parajson(request):
    data = BarangWishlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def paraxmlid(request, id):
    data = BarangWishlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def parajsonid(request, id):
    data = BarangWishlist.objects.filter(pk=id)  
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")  

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('wishlist:login_user')
    
    context = {'form':form}
    return render(request, 'register.html', context)
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("wishlist:show_wishlist"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('wishlist:login_user'))
    response.delete_cookie('last_login')
    return response
# Create your views here.
