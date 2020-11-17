from django.urls import path, include
from .views import home,lista_produtos, access_produto


urlpatterns = [
    path('', home, name='home'),
    path('produtos/', lista_produtos, name='lista_produtos'),
    path('produtos/<int:id>/', access_produto , name='access_produto'),
    path('cadastro/', include('users.urls')),
    path('carrinho/', include('carrinho.urls')),
]
