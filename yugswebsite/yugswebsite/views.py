from django import forms
from django.http import HttpResponse
from django.shortcuts import render_to_response,render
from django.template import Template,Context
from django.template.loader import get_template
from mainapp.models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.template import RequestContext
import mainapp.models
from django.shortcuts import redirect


#some fake data//dummy data, so no need to save in database
categories={
    'mens':[{'name':'Aveeno','cost':500,'imagename':'aveeno.jpg'},
            {'name':'Aveeno 2','cost':600,'imagename':'aveeno2.jpg'},
            {'name':'Bblunt','cost':850,'imagename':'bblunt.png'},
            {'name':'Dermacontrol','cost':300,'imagename':'dermacontrol.png'}
            ],
    'moisturising':[{'name':'Night cream','cost':709,'imagename':'white perfect.jpg'},
            {'name':'Olay Total Effects','cost':760,'imagename':'olay total effects.jpg'},
            {'name':'Olay Regenerist','cost':999,'imagename':'olay regenerist.jpg'},
            {'name':'Age Protect','cost':1000,'imagename':'age protect.jpg'}
            ],
    'cleansing':[{'name':'Lotus Herbals','cost':259,'imagename':'lotush.jpg'},
            {'name':'Avene Micellar','cost':1020,'imagename':'avene.jpg'},
            {'name':'Maybelline Total Clean','cost':850,'imagename':'mbln.jpg'},
            {'name':'Loreal Paris Dermo','cost':300,'imagename':'lorealdermo.jpg'}
            ]
    }



def index(request):
    if request.method=="GET":
        if 'q' in request.GET:
            required_list=list(Product.objects.filter(category=request.GET['q']))
            return render(request,'home.html',{'items':required_list})
    return render(request,'home.html',{'items':list(Product.objects.filter(category="mens"))})


def contact(request):
    return render(request,'contact.html')

def signup_page(request):
    return render(request, 'signup.html')

def login(request):
    username=request.POST.get('email',"")
    password=request.POST.get('password',"")
    user=auth.authenticate(username=username,password=password)
    if user is not None and user.is_active:
        auth.login(request,user)
        return render(request,'home.html',{'items':list(Product.objects.filter(category="mens"))})
    else:
        return HttpResponse("Login error.")

    
def signup(request):
    user=None
    if request.method=='POST':
        try:
           user=User.objects.create_user(username=request.POST.get('email',""),
                                      email=request.POST.get('email',""),
                                      password=request.POST.get('password',""))
           user.save()
           user_object=mainapp.models.User(name=request.POST.get('name',""),
                                        email=request.POST.get('email',""),
                                        contact=request.POST.get('contact',""),
                                        address=request.POST.get('address',""),
                                        password=request.POST.get('password',""))
           user_object.save()#save to database
           login(request)
           return render(request,'home.html',{'items':list(Product.objects.filter(category="mens"))})
        except:
            if user is not None:
                user.delete()
            return HttpResponse("User Already exists")
   
def logout(request):
    auth.logout(request)
    return render(request,'home.html',{'items':list(Product.objects.filter(category="mens"))})

@login_required
def addtokart(request):    
    if 'q' in request.GET:
        try:
            product_name=Product.objects.filter(product_name=request.GET['q'])[0].product_name
            k=Kart(email=request.user.username,product_name=product_name)
            k.save()
            return render(request,'home.html',{'items':list(Product.objects.filter(category="mens"))})
        except:
            return HttpResponse("Product already in kart")


@login_required
def addtowishlist(request):
    if 'q' in request.GET:
        try:
           product_name=Product.objects.filter(product_name=request.GET['q'])[0].product_name
           w=Wishlist(email=request.user.username,product_name=product_name)
           w.save()
           return render(request,'home.html',{'items':list(Product.objects.filter(category="mens"))})
        except:
            return HttpResponse("Product already in wishlist")

@login_required
def showwishlist(request):
    wishlist=Wishlist.objects.filter(email=request.user.username)
    if wishlist is not None and len(wishlist)>0:
        return render(request,'showwishlist.html',{'wishlist':wishlist})
    else:
        return HttpResponse("YOU HAVE AN EMPTY WISHLIST")

@login_required  
def showkart(request):
    kart=Kart.objects.filter(email=request.user.username)
    if kart is not None and len(kart)>0:
        return render(request,'showkart.html',{'kart':kart})
    else:
        return HttpResponse("YOU HAVE AN EMPTY KART")

def redirect_to_login_modal(request):
    return render(request,'home.html',{'items':list(Product.objects.filter(category="mens")),'signinsignal':True})
        











