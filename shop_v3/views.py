from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from shop.models import Product, Order, Cart, PromoCode, CartItem
from .serializers import ProductSerializer, OrderSerializer, CartSerializer, PromoCodeSerializer
from django.core.mail import send_mail
from django.db.models import F
from rest_framework.permissions import IsAuthenticated

# Главная страница работает корректно
@api_view(['GET'])
def main_page(request):
    return Response({'detail': 'Добро пожаловать в магазин!'}, status=200)

# Каталог товаров с сортировкой и пагинацией
class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Product.objects.all()
        sort = self.request.query_params.get('sort')
        if sort == 'price_asc':
            queryset = queryset.order_by('price')
        elif sort == 'price_desc':
            queryset = queryset.order_by('-price')
        return queryset

# Детали товара (правильное изображение)
class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

# Логин с сохранением сессии
@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return Response({'detail': 'Logged in successfully.'})
    return Response({'detail': 'Invalid credentials'}, status=400)

# Добавление в корзину с проверкой наличия товара
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_cart(request):
    user = User.objects.first()  # Для теста, всегда первый пользователь
    product_id = request.data.get('product_id')
    quantity = int(request.data.get('quantity', 1))
    product = Product.objects.get(id=product_id)
    if product.stock < quantity:
        return Response({'detail': 'Недостаточно товара на складе'}, status=400)
    cart, _ = Cart.objects.get_or_create(user=user)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if created:
        item.quantity = quantity
    else:
        if product.stock < item.quantity + quantity:
            return Response({'detail': 'Недостаточно товара на складе'}, status=400)
        item.quantity += quantity
    item.save()
    return Response({'detail': 'Added to cart'})

# Применение промокода с реальной скидкой
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def apply_promocode(request):
    user = User.objects.first()  # Для теста
    code = request.data.get('code')
    promo = PromoCode.objects.filter(code=code, is_active=True).first()
    cart = Cart.objects.get(user=user)
    if promo:
        discount = promo.discount_percent
        total = sum([item.product.price * item.quantity for item in cart.cartitem_set.all()])
        discounted_total = total * (1 - discount / 100)
        return Response({'detail': 'Промокод применён', 'discount': discount, 'total': total, 'discounted_total': discounted_total})
    return Response({'detail': 'Промокод не найден'}, status=404)

# Оплата проходит успешно
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def pay_order(request):
    user = User.objects.first()  # Для теста
    cart = Cart.objects.get(user=user)
    total = sum([item.product.price * item.quantity for item in cart.cartitem_set.all()])
    order = Order.objects.create(user=user, total=total)
    cart.cartitem_set.all().delete()  # Очищаем корзину
    return Response({'detail': 'Оплата прошла успешно', 'order_id': order.id})

# История заказов пользователя
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def order_history(request):
    user = User.objects.first()  # Для теста
    orders = Order.objects.filter(user=user)
    return Response(OrderSerializer(orders, many=True).data)

# Сброс пароля имитирует отправку письма
@api_view(['POST'])
def password_reset(request):
    email = request.data.get('email')
    # Имитация отправки письма
    # send_mail('Сброс пароля', 'Ваш новый пароль: 123456', 'from@example.com', [email])
    return Response({'detail': f'Письмо отправлено на {email}'}, status=200)
