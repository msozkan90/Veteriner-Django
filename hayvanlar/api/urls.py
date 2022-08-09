from django.urls import path

from hayvanlar.api import views as api_views
urlpatterns = [
    path('animals/',api_views.AnimalsListCreateAPIView.as_view(),name='animalslist'),
    path('owners/',api_views.OwnersListCreateAPIView.as_view(),name='ownerslist'),
    path('animals/<int:pk>',api_views.AnimalsDetailCreateAPIView.as_view(),name='animalsdetail'),
    path('owners/<int:pk>',api_views.OwnersDetailCreateAPIView.as_view(),name='ownersdetail'),
 

]