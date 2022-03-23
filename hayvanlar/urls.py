
from django.urls import path

from . import views
app_name="hayvanlar"

urlpatterns = [
    path('', views.index, name="index"),
    path('animals', views.animals, name="animals"),
    path('animalowners/', views.owners, name="animalowners"),
    path('animal-delete/<int:id>',views.animal_delete,name = "animal_delete"),
    path('owner-delete/<int:id>',views.owner_delete,name = "owner_delete"),
    path('animal/update/<int:id>/',views.animal_update,name="animal-update"),
    path('animal/detail/<int:id>/',views.animal_detail,name="animal_detail"),
    path('owner/detail/<int:id>/',views.owner_detail,name="owner_detail"),
    path('owner/update/<int:id>',views.owner_update, name = "owner-update"),
    path('warning',views.alertmessage, name = "alertmessage"),


]