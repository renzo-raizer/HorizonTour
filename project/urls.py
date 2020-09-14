from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # alterar products para o nome da pasta
    path('', include('posts.urls')),
    path('sobre/', include('sobre.urls')),
    path('accounts/', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]