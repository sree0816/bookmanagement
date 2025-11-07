from django.urls  import path
from adminapp import views
urlpatterns=[path('index/',views.index,name='index'),
             path('add_book/',views.add_book,name='add_book'),
             path('add_category/',views.add_category,name='add_category'),
             path('save_category/',views.save_category,name='save_category'),
             path('display_category/',views.display_category,name='display_category'),
             path('delete_category/<int:cid>',views.delete_category,name='delete_category'),
             path('update_category/<int:cid>',views.update_category,name='update_category'),
             path('edit_category/<int:cid>',views.edit_category,name='edit_category'),
             path('save_books/',views.save_books,name='save_books'),
             path('display_book/',views.display_book,name='display_book'),
             path('edit_book/<int:bid>',views.edit_book,name='edit_book'),
             path('delete_book/<int:bid>',views.delete_book,name='delete_book'),
             path('update_book/<int:bid>',views.update_book,name='update_book'),
             path('loginpage/',views.loginpage,name='loginpage'),
             path('admin_login/',views.admin_login,name='admin_login'),
             path('admin_logout/',views.admin_logout,name='admin_logout')]
