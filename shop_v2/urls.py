from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from shop_backend.settings import SITE_URL

from . import views

# Собираем только свои маршруты для Swagger
v2_patterns = [
    path("", views.main_page),  # Главная страница работает
    path("products/", views.ProductListView.as_view()),  # Каталог товаров работает
    path(
        "products/<int:pk>/", views.ProductDetailView.as_view()
    ),  # Детали товара (ошибка Major сохранена)
    path("login/", views.login_view),  # Логин с сессией
    path("cart/add/", views.add_to_cart),  # Остальные баги сохранены
    path("cart/apply-promocode/", views.apply_promocode),
    path("pay/", views.pay_order),
    path("orders/history/", views.order_history),
    path("password-reset/", views.password_reset),
    # Djoser auth endpoints (регистрация, токены, и т.д.)
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
    path("auth/", include("djoser.urls.jwt")),
]

schema_view = get_schema_view(
    openapi.Info(
        title="Shop API v2",
        default_version="v2",
        description="Документация API v2 (без Blocker-ошибок)",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    patterns=v2_patterns,
    url=f"{SITE_URL}/api_v2/",
)

urlpatterns = v2_patterns + [
    # Swagger/OpenAPI
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
