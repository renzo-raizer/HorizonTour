from django.urls import path
from . import views
from .views import update, del_perfil, perfil

urlpatterns = [
    path('register/', views.SignUp.as_view(), name='signup'),
    path('delete/', del_perfil, name='del_perfil'),
    path('update/', update, name= 'update_user'),
    path('perfil/', perfil, name='perfil'),
    path('perfil/', perfil, name='endereco'),    
]