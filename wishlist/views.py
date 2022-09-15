from django.shortcuts import render
from wishlist.models import BarangWishlist
from django.http import HttpResponse
from django.core import serializers
def show_wishlist(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    context = {
        'list_barang': data_barang_wishlist,
        'nama': 'Sayyid Hafidzurrahman Atstsaqofi'
    }
    return render(request, "wishlist.html", context)
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
# Create your views here.
