from django.urls import path
from webapp import views

urlpatterns=[path('home/',views.home,name='home'),
             path('about_page/',views.about_page,name='about_page'),
             path('popular/',views.popular,name='popular'),
             path('contact/',views.contact,name='contact'),
             path('checkout/',views.checkout,name='checkout'),
             path('filtered/<cat>/',views.filtered,name='filtered'),
             path('single_book/<int:bid>',views.single_book,name='single_book')]