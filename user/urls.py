
from django.urls import path
from . import views
# from .views import UserCreateView,UserLoginView
app_name="user"

urlpatterns = [
    path('login/', views.sign_in, name="sign_in"),
    path('register/', views.register, name="register"),
    path('logout/', views.sign_out, name="sign_out"),

    # path('login/', UserLoginView.as_view(), name="sign_in"),
    # path('register/', UserCreateView.as_view(), name="register"),

]