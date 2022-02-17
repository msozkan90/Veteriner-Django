from django.contrib import admin
from django.urls import path

from . import views
app_name="hayvanlar"

urlpatterns = [
    path('', views.index, name="index"),
    path('hayvanlar/', views.hayvanlar, name="animals"),
    path('hayvanSahipleri/', views.sahipler, name="hayvanSahipleri"),
    path('hayvan-delete/<int:id>',views.hayvan_delete,name = "hayvan_delete"),
    path('sahip-delete/<int:id>',views.sahipler_delete,name = "sahipler_delete"),
    path('hayvan/update/<int:id>/',views.hayvan_update,name="hayvan-update"),
    path('hayvan/detay/<int:id>/',views.hayvan_detay,name="hayvanDetay"),
    path('sahip/detay/<int:id>/',views.sahip_detay,name="sahipDetay"),
    path('sahip/update/<int:id>',views.sahipler_update, name = "sahip-update"),
    path('uyarı',views.alertmessage, name = "alertmessage"),


]