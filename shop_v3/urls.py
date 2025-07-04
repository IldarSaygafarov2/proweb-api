from django.urls import path, include
from . import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Собираем только свои маршруты для Swagger
v3_patterns = [
    path('', views.main_page),  # Главная страница
    path('products/', views.ProductListView.as_view()),  # Каталог товаров
    path('products/<int:pk>/', views.ProductDetailView.as_view()),  # Детали товара
    path('login/', views.login_view),  # Логин
    path('cart/add/', views.add_to_cart),  # Добавление в корзину
    path('cart/apply-promocode/', views.apply_promocode),  # Применение промокода
    path('pay/', views.pay_order),  # Оплата
    path('orders/history/', views.order_history),  # История заказов
    path('password-reset/', views.password_reset),  # Сброс пароля
    # Djoser auth endpoints (регистрация, токены, и т.д.)
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
]

schema_view = get_schema_view(
    openapi.Info(
        title="Shop API v3",
        default_version='v3',
        description="Документация API v3 (без ошибок)",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    patterns=v3_patterns,
)

urlpatterns = v3_patterns + [
    # Swagger/OpenAPI
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] 