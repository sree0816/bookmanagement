from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
import datetime


# Create your views here.


from adminapp.models import CategoryDB, BookDB


# Create your views here.
def index(request):
    categories=CategoryDB.objects.count()
    books=BookDB.objects.count()
    date=datetime.datetime.now()
    return render(request,'index.html',{'categories':categories,'books':books,'date':date})
def add_book(request):
    categories=CategoryDB.objects.all()
    return render(request,'add_book.html',{'categories':categories})
def add_category(request):
    return render(request,'add_category.html')
def save_category(request):
    if request.method=='POST':
        n=request.POST.get('cname')
        d=request.POST.get('cdesc')
        img=request.FILES['ccoverimage']
        obj=CategoryDB(name=n,description=d,coverimage=img)
        obj.save()
    return redirect(add_category)
def display_category(request):
    date = datetime.datetime.now()
    data=CategoryDB.objects.all()
    return render(request,'display_category.html',{'data':data})
def delete_category(request,cid):
    data=CategoryDB.objects.get(id=cid)
    data.delete()
    return redirect(display_category)
def update_category(request,cid):
    if request.method=='POST':
        n=request.POST.get('cname')
        d=request.POST.get('cdesc')
        try:
            img=request.FILES['ccoverimage']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=CategoryDB.objects.get(id=cid).coverimage
        CategoryDB.objects.filter(id=cid).update(name=n,description=d,coverimage=file)
    return redirect(display_category)
def edit_category(request,cid):
    data=CategoryDB.objects.get(id=cid)
    return render(request,'edit_category.html',{'data':data})
def save_books(request):
    if request.method=='POST':
        t=request.POST.get('title')
        a=request.POST.get('author')
        c=request.POST.get('category')
        p=request.POST.get('price')
        pub=request.POST.get('publisher')
        d=request.POST.get('description')
        i=request.FILES['coverimage']
        obj=BookDB(title=t,author=a,category=c,price=p,publisher=pub,description=d,coverimage=i)
        obj.save()
    return redirect(add_book)

def display_book(request):
    data=BookDB.objects.all()
    return render(request,'display_book.html',{'data':data})
def delete_book(request,bid):
    data=BookDB.objects.get(id=bid)
    data.delete()
    return redirect(display_book)
def edit_book(request,bid):
    categories=CategoryDB.objects.all()
    data=BookDB.objects.get(id=bid)
    return render(request,'edit_book.html',{'data':data,'categories':categories})
def update_book(request,bid):
    if request.method=='POST':
        t=request.POST.get('title')
        a=request.POST.get('author')
        c=request.POST.get('category')
        p=request.POST.get('price')
        pub=request.POST.get('publisher')
        d=request.POST.get('description')
        try:
            img=request.FILES['coverimage']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=BookDB.objects.get(id=bid).coverimage
        BookDB.objects.filter(id=bid).update(title=t,author=a,category=c,price=p,publisher=pub,description=d,coverimage=file)
    return redirect(display_book)
def loginpage(request):
    return render(request,'login.html')
def admin_login(request):
    if request.method=='POST':
        u=request.POST.get('username')
        p=request.POST.get('password')
        if User.objects.filter(username__contains=u).exists():
            data=authenticate(username=u,password=p)
            if data is not None:
                login(request,data)
                request.session['username']=u
                request.session['password']=p
                return redirect(index)
            else:
                return redirect(loginpage)
        else:
            return redirect(loginpage)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(loginpage)
