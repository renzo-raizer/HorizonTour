from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # alterar products para o nome da pasta
    path('', include('posts.urls')),
    path('accounts/', include('users.urls')),
    path('carrinho/', include('carrinho.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('social_django.urls', namespace='social')),
]