from django.shortcuts import render,redirect
from adminapp.models import CategoryDB, BookDB
from webapp.models import SignupDB, ContactDB


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

def save_signup(request):
    if request.method=='POST':
        n=request.POST.get('username')
        e=request.POST.get('email')
        p=request.POST.get('password')
        c=request.POST.get('confirmpass')
        m=request.POST.get('mobile')
        obj=SignupDB(name=n,email=e,password=p,confirmpass=c,mobile=m)
        obj.save()
    return redirect(sign_in)
def user_login(request):
    if request.method=='POST':
        n=request.POST.get('username')
        p=request.POST.get('password')
        if SignupDB.objects.filter(name=n,password=p).exists():
            request.session['name']=n
            request.session['password']=p
            return redirect(home)
        else:
            return redirect(sign_in)
    else:
        return redirect(sign_in)

def user_logout(request):
    del request.session['name']
    del request.session['password']
    return redirect(sign_in)

def save_message(request):
    if request.method=='POST':
        n=request.POST.get('name')
        m=request.POST.get('mail')
        s=request.POST.get('subject')
        message=request.POST.get('message')
        obj=ContactDB(name=n,email=m,subject=s,message=message)
        obj.save()
    return redirect(contact)

