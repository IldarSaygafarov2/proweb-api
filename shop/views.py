from django.shortcuts import render
from rest_framework import generics, status, permissions, views
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Product, Order, Cart, PromoCode, CartItem
from .serializers import ProductSerializer, OrderSerializer, CartSerializer, PromoCodeSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import time

# Create your views here.

# S1: Главная страница всегда возвращает 503 Service Unavailable
@api_view(['GET'])
def main_page(request):
    return Response({'detail': 'Service Unavailable'}, status=503)

# S1: Каталог товаров не отвечает (бесконечная загрузка)
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        time.sleep(1000)  # Имитация бесконечной загрузки
        return super().list(request, *args, **kwargs)

# S3: Сортировка товаров по цене не работает (игнорируется)
# S3: Пагинация сломана (всегда первая страница)
# S3: Изображения перепутаны (всегда одно и то же фото)
class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.image_url = 'https://wrong.image.url/other.jpg'
        return Response(ProductSerializer(instance).data)

# S1: После логина не сохраняется сессия/токен
@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        return Response({'detail': 'Logged in, but no session.'})
    return Response({'detail': 'Invalid credentials'}, status=400)

# S2: Можно добавить в корзину товар, которого нет в наличии
@api_view(['POST'])
def add_to_cart(request):
    user = User.objects.first()
    product_id = request.data.get('product_id')
    quantity = int(request.data.get('quantity', 1))
    product = Product.objects.get(id=product_id)
    cart, _ = Cart.objects.get_or_create(user=user)
    item, _ = CartItem.objects.get_or_create(cart=cart, product=product)
    item.quantity += quantity
    item.save()
    return Response({'detail': 'Added to cart'})

# S2: Промокод не применяется (скидка не меняет сумму)
@api_view(['POST'])
def apply_promocode(request):
    code = request.data.get('code')
    promo = PromoCode.objects.filter(code=code, is_active=True).first()
    if promo:
        return Response({'detail': 'Промокод применён', 'discount': promo.discount_percent})
    return Response({'detail': 'Промокод не найден'}, status=404)

# S2: Система оплаты не работает (всегда ошибка)
@api_view(['POST'])
def pay_order(request):
    return Response({'detail': 'Ошибка оплаты'}, status=500)

# S3: История заказов не отображается (пусто)
@api_view(['GET'])
def order_history(request):
    return Response([])

# S3: "Забыли пароль" — письмо не приходит
@api_view(['POST'])
def password_reset(request):
    return Response({'detail': 'Письмо отправлено'}, status=200)
