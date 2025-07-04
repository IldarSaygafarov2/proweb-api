# Импорт базового класса моделей Django
from django.db import models  # Для создания моделей
# Импорт стандартной модели пользователя Django
from django.contrib.auth.models import User  # Для связи заказов и корзин с пользователем

# Модель категории
class Category(models.Model):
    name = models.CharField(max_length=100)  # Название категории
    description = models.TextField(blank=True)  # Описание категории

    def __str__(self):
        return self.name

# Модель товара
class Product(models.Model):
    name = models.CharField(max_length=255)  # Название товара
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена товара
    stock = models.PositiveIntegerField(default=0)  # Количество на складе
    image_url = models.URLField(blank=True, null=True)  # URL изображения товара
    # Опечатка в характеристике
    diaganal = models.CharField(max_length=100, default='15.6')  # S5: "Диаганаль"
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True, blank=True)  # Категория товара

    def __str__(self):
        return self.name  # Возвращает название товара при печати объекта

# Модель промокода
class PromoCode(models.Model):
    code = models.CharField(max_length=50, unique=True)  # Код промокода
    discount_percent = models.PositiveIntegerField(default=0)  # Процент скидки
    is_active = models.BooleanField(default=True)  # Активен ли промокод

# Модель заказа
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Пользователь, сделавший заказ
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания заказа
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Итоговая сумма заказа
    promo_code = models.ForeignKey(PromoCode, on_delete=models.SET_NULL, null=True, blank=True)  # Применённый промокод

# Модель корзины
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Корзина привязана к одному пользователю
    products = models.ManyToManyField(Product, through='CartItem')  # Товары в корзине через промежуточную модель

# Промежуточная модель для товаров в корзине
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)  # Корзина
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Товар
    quantity = models.PositiveIntegerField(default=1)  # Количество товара
