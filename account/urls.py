from django.urls import path

from . import views
urlpatterns = [
    path('',views.index),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('signuppage',views.signuppage,name='signuppage'),
    path('login',views.login,name='login'),
    path('userhome',views.userhome,name='userhome'),
    path('logout',views.logout,name='logout')
]
