from django.shortcuts import render
from adminapp.models import CategoryDB, BookDB


# Create your views here.
def home(request):
    categories=CategoryDB.objects.all()
    return render(request,'home.html',{'categories':categories})
def about_page(request):
    categories = CategoryDB.objects.all()
    return render(request,'about.html',{'categories':categories})
def popular(request):
    book=BookDB.objects.all()
    categories = CategoryDB.objects.all()
    return render(request,'popular.html',{'categories':categories,'book':book})
def contact(request):
    categories = CategoryDB.objects.all()
    return render(request,'contactus.html',{'categories':categories})
def checkout(request):
    categories=CategoryDB.objects.all()
    return render(request,'checkout.html',{'categories':categories})

def filtered(request,cat):
    books=BookDB.objects.filter(category=cat)
    categories=CategoryDB.objects.all()
    return render(request,'filtered.html',{'books':books,'categories':categories,'cat':cat })

def single_book(request,bid):
    book=BookDB.objects.get(id=bid)
    categories=CategoryDB.objects.all()
    return render(request,'single_book.html',{'book':book,'categories':categories})

def sign_in(request):
    return render(request,'sign_in.html')

def sign_up(request):
    return render(request,'sign_up.html')
