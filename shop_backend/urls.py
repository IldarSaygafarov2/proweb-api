"""
URL configuration for shop_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Импорт админки Django
from django.contrib import admin  # Для доступа к административной панели
# Импорт функций path и include для маршрутизации
from django.urls import path, include  # Для описания маршрутов

# Основные маршруты проекта
urlpatterns = [
    path('admin/', admin.site.urls),  # Маршрут для административной панели
    path('api_v1/', include('shop.urls')),  # v1 API с ошибками Blocker
    path('api_v2/', include('shop_v2.urls')),  # v2 API без ошибок Blocker
    path('api_v3/', include('shop_v3.urls')),  # v3 API без ошибок вообще
]
