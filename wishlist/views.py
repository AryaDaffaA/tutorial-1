from django.shortcuts import render
from wishlist.models import BarangWishlist
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_wishlist(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    context = {
    'list_barang': data_barang_wishlist,
    'nama': 'Arya Daffa'
}   
    return render(request, "wishlist.html", context)

def xml_funct(request):
    data = BarangWishlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def json_funct(request):
    data = BarangWishlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def id_funct_xml(request, id):
    data = BarangWishlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def id_funct_json(request, id):
    data = BarangWishlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
   
    

