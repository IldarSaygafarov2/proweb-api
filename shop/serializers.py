# Импорт базового класса сериализаторов DRF
from rest_framework import serializers  # Для создания сериализаторов
from .models import Product, Order, Cart, PromoCode, CartItem, Category  # Импорт моделей

# Сериализатор для модели Category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']
        ref_name = 'CategoryShop'

# Сериализатор для модели Product
class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Product  # Модель, с которой работает сериализатор
        fields = ['id', 'name', 'price', 'stock', 'image_url', 'diaganal', 'category']  # Все поля товара, включая опечатку и категорию
        ref_name = 'ProductShop'

# Сериализатор для модели PromoCode
class PromoCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromoCode  # Модель промокода
        fields = ['id', 'code', 'discount_percent', 'is_active']  # Все поля промокода

# Сериализатор для модели Order
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order  # Модель заказа
        fields = ['id', 'user', 'created_at', 'total', 'promo_code']  # Все поля заказа

# Сериализатор для промежуточной модели CartItem
class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()  # Вложенный сериализатор товара
    class Meta:
        model = CartItem  # Модель CartItem
        fields = ['id', 'product', 'quantity']  # Все поля CartItem

# Сериализатор для модели Cart
class CartSerializer(serializers.ModelSerializer):
    products = CartItemSerializer(source='cartitem_set', many=True)  # Все товары в корзине через CartItem
    class Meta:
        model = Cart  # Модель корзины
        fields = ['id', 'user', 'products']  # Все поля корзины 