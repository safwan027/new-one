from django.urls import path
from . import views

urlpatterns = [
    path('userhome/',views.user_home,name='userhome'),
    path('bookdetails/<int:id>/',views.book_details,name='bookdetails'),
    path('editcomment/<int:id>/',views.edit_comment,name='editcomment'),
    path('deletecomment/<int:id>/',views.delete_comment,name='deletecomment'),
    path('adminhome/',views.admin_home,name='adminhome'),
    path('addbook/',views.add_book,name='addbook'),
    path('deletebook/<int:id>/',views.delete_book,name='deletebook'),
    path('editbook/<int:id>/',views.edit_book,name='editbook'),
    #path('publish/',views.publish,name='publish'),
    path('register/',views.register,name='register'),
    path('',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
]