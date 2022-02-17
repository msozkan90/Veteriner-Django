from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
app_name="user"

urlpatterns = [
    
    path('login/', views.sign_in, name="sign_in"),
    path('logout/', views.sign_out, name="sign_out"),
    path('register/', views.register, name="register"),

]