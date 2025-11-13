from django.urls import path
from webapp import views

urlpatterns=[path('home/',views.home,name='home'),
             path('about_page/',views.about_page,name='about_page'),
             path('popular/',views.popular,name='popular'),
             path('contact/',views.contact,name='contact'),
             path('checkout/',views.checkout,name='checkout'),
             path('filtered/<cat>/',views.filtered,name='filtered'),
             path('single_book/<int:bid>',views.single_book,name='single_book'),
             path('sign_in/',views.sign_in,name='sign_in'),
             path('sign_up/',views.sign_up,name='sign_up'),
             path('save_signup/',views.save_signup,name='save_signup'),
             path('user_login/',views.user_login,name='user_login'),
             path('user_logout/', views.user_logout, name='user_logout'),
             path('save_message/',views.save_message,name='save_message')

             ]