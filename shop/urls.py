# Импорт функции path для маршрутизации
from django.urls import path, include  # Для описания маршрутов
from . import views  # Импортируем views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from shop_backend.settings import SITE_URL

# Основные маршруты API магазина
urlpatterns = [
    path('', views.main_page),  # S1: Главная страница всегда 503 (Blocker)
    path('products/', views.ProductListView.as_view()),  # S1: Каталог товаров не отвечает (Blocker)
    path('products/<int:pk>/', views.ProductDetailView.as_view()),  # S3: Перепутанное изображение товара (Major)
    path('login/', views.login_view),  # S1: После логина не сохраняется сессия/токен (Blocker)
    path('cart/add/', views.add_to_cart),  # S2: Можно добавить товар без проверки наличия (Critical)
    path('cart/apply-promocode/', views.apply_promocode),  # S2: Промокод не меняет сумму (Critical)
    path('pay/', views.pay_order),  # S2: Оплата всегда ошибка (Critical)
    path('orders/history/', views.order_history),  # S3: История заказов всегда пусто (Major)
    path('password-reset/', views.password_reset),  # S3: Письмо не отправляется (Major)
]

# Собираем только свои маршруты для Swagger
v1_patterns = [
    path('', views.main_page),
    path('products/', views.ProductListView.as_view()),
    path('products/<int:pk>/', views.ProductDetailView.as_view()),
    path('login/', views.login_view),
    path('cart/add/', views.add_to_cart),
    path('cart/apply-promocode/', views.apply_promocode),
    path('pay/', views.pay_order),
    path('orders/history/', views.order_history),
    path('password-reset/', views.password_reset),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
]

schema_view = get_schema_view(
    openapi.Info(
        title="Shop API v1",
        default_version='v1',
        description="Документация API v1 (с ошибками)",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    patterns=v1_patterns,
    url=f"{SITE_URL}/api_v1/",
)

urlpatterns = v1_patterns + [
    # Swagger/OpenAPI
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]