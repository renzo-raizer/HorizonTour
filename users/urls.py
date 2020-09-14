from django.urls import path
from . import views
from .views import perfil, del_perfil, update_user

urlpatterns = [
    path('register/', views.SignUp.as_view(), name='signup'),
    path('delete/', del_perfil, name='del_perfil'),
    path('update/', update_user, name= 'update_user'),
    path('perfil/', perfil, name='perfil'),
]