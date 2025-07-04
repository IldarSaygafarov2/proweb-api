from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from shop.models import Product, Order, Cart, PromoCode, CartItem
from .serializers import ProductSerializer, OrderSerializer, CartSerializer, PromoCodeSerializer
from rest_framework.permissions import IsAuthenticated

# Главная страница работает корректно (нет ошибки Blocker)
@api_view(['GET'])
def main_page(request):
    return Response({'detail': 'Добро пожаловать в магазин!'}, status=200)

# Каталог товаров отвечает корректно (нет ошибки Blocker)
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    # S3: Сортировка и пагинация по-прежнему не работают (Major)
    # S3: Можно реализовать так же, как в shop, если нужно оставить баги

# Детали товара (оставим ошибку с изображением, если нужно)
class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.image_url = 'https://wrong.image.url/other.jpg'  # S3: перепутанное изображение (Major)
        return Response(ProductSerializer(instance).data)

# Логин с сохранением сессии (нет ошибки Blocker)
@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)  # Сохраняем сессию
        return Response({'detail': 'Logged in successfully.'})
    return Response({'detail': 'Invalid credentials'}, status=400)

# Остальные view-функции можно скопировать из shop/views.py, чтобы оставить баги Critical и Major
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_cart(request):
    user = User.objects.first()  # Для теста, всегда первый пользователь
    product_id = request.data.get('product_id')
    quantity = int(request.data.get('quantity', 1))
    product = Product.objects.get(id=product_id)
    cart, _ = Cart.objects.get_or_create(user=user)
    item, _ = CartItem.objects.get_or_create(cart=cart, product=product)
    item.quantity += quantity
    item.save()
    return Response({'detail': 'Added to cart'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def apply_promocode(request):
    code = request.data.get('code')
    promo = PromoCode.objects.filter(code=code, is_active=True).first()
    if promo:
        return Response({'detail': 'Промокод применён', 'discount': promo.discount_percent})
    return Response({'detail': 'Промокод не найден'}, status=404)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def pay_order(request):
    return Response({'detail': 'Ошибка оплаты'}, status=500)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def order_history(request):
    return Response([])

@api_view(['POST'])
def password_reset(request):
    return Response({'detail': 'Письмо отправлено'}, status=200)
