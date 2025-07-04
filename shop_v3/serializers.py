from rest_framework import serializers  # Для создания сериализаторов
from shop.models import Product, Order, Cart, PromoCode, CartItem, Category  # Импорт моделей из shop

# Сериализатор для модели Category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']
        ref_name = 'CategoryShopV3'

# Сериализатор для модели Product
class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'stock', 'image_url', 'diaganal', 'category']
        ref_name = 'ProductShopV3'

# Сериализатор для модели PromoCode
class PromoCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromoCode
        fields = ['id', 'code', 'discount_percent', 'is_active']

# Сериализатор для модели Order
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'created_at', 'total', 'promo_code']

# Сериализатор для промежуточной модели CartItem
class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity']

# Сериализатор для модели Cart
class CartSerializer(serializers.ModelSerializer):
    products = CartItemSerializer(source='cartitem_set', many=True)
    class Meta:
        model = Cart
        fields = ['id', 'user', 'products'] 