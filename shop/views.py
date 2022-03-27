
from django.shortcuts import render
from django.http import HttpResponse
from .models import product ,Contact , Checkout
from math import ceil
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

def index(request):
    # products = product.objects.all()
    # print(products)
    # n = len(products)
    # nslide = n//4 + ceil((n/4)-(n//4))
    # # params = {'no_of_slides': nslide, 'range': range(1,nslide) ,'product':products}
    # allprod = [[products, range(1, nslide), nslide],
    #           [products, range(1, nslide), nslide]]

    allprod = []
    catprods = product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = product.objects.filter(category = cat)
        n = len(prod)
        nslide = n//4 + ceil((n/4)-(n//4))
        allprod.append([prod,range(1,nslide),nslide])

    params = {'allprod' : allprod}
    return render(request,'shop/index.html',params)


def about(request):
    return render(request,'shop/about.html')


def contact(request):
    if request.method=="POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        contact = Contact(name=name, email=email , phone=phone , desc=desc)
        contact.save()

    return render(request,'shop/contact.html')


def tracker(request):
    return render(request,'shop/tracker.html')


def search(request):
    return render(request,'shop/search.html')


def productview(request, myid):
    prod = product.objects.filter(id = myid)
    print(prod)

    return render(request,'shop/productview.html', {'product':prod[0]})


def productpre(request):
    return render(request,'shop/productpre.html')

def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        address = request.POST.get('address','')
        address2 = request.POST.get('address2','')
        city = request.POST.get('city','')
        state = request.POST.get('state','')
        zip = request.POST.get('zip','')
        phone = request.POST.get('phone','')
        checkout = Checkout(items_json=items_json, name=name, email=email,address = address, address2 = address2 , city =city, state = state , zip = zip , phone = phone)
        checkout.save()
        thank = True
        id = Checkout.msg_id
        return render(request, 'shop/checkout.html', {'thank': thank, 'id': id})
    return render(request, 'shop/checkout.html')





