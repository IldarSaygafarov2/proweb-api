import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop_backend.settings')
django.setup()

from shop.models import Category, Product

categories = [
    {'name': 'Смартфоны', 'description': 'Мобильные телефоны и смартфоны'},
    {'name': 'Ноутбуки', 'description': 'Персональные ноутбуки для работы и учебы'},
    {'name': 'Телевизоры', 'description': 'Современные телевизоры разных диагоналей'},
    {'name': 'Планшеты', 'description': 'Планшетные компьютеры для развлечений и работы'},
    {'name': 'Аксессуары', 'description': 'Чехлы, зарядки, кабели и другие аксессуары'},
]

products = [
    # Смартфоны
    [
        {'name': 'iPhone 14', 'price': 79990, 'stock': 10, 'image_url': 'https://example.com/iphone14.jpg', 'diaganal': '6.1'},
        {'name': 'Samsung Galaxy S23', 'price': 69990, 'stock': 15, 'image_url': 'https://example.com/galaxy_s23.jpg', 'diaganal': '6.1'},
        {'name': 'Xiaomi 13', 'price': 49990, 'stock': 20, 'image_url': 'https://example.com/xiaomi13.jpg', 'diaganal': '6.36'},
        {'name': 'Google Pixel 7', 'price': 59990, 'stock': 8, 'image_url': 'https://example.com/pixel7.jpg', 'diaganal': '6.3'},
        {'name': 'OnePlus 11', 'price': 54990, 'stock': 12, 'image_url': 'https://example.com/oneplus11.jpg', 'diaganal': '6.7'},
    ],
    # Ноутбуки
    [
        {'name': 'MacBook Air M2', 'price': 119990, 'stock': 5, 'image_url': 'https://example.com/macbookair.jpg', 'diaganal': '13.6'},
        {'name': 'Dell XPS 13', 'price': 99990, 'stock': 7, 'image_url': 'https://example.com/dellxps13.jpg', 'diaganal': '13.4'},
        {'name': 'HP Spectre x360', 'price': 89990, 'stock': 6, 'image_url': 'https://example.com/hpspectre.jpg', 'diaganal': '13.5'},
        {'name': 'Lenovo ThinkPad X1', 'price': 109990, 'stock': 4, 'image_url': 'https://example.com/thinkpadx1.jpg', 'diaganal': '14'},
        {'name': 'ASUS ZenBook 14', 'price': 84990, 'stock': 9, 'image_url': 'https://example.com/zenbook14.jpg', 'diaganal': '14'},
    ],
    # Телевизоры
    [
        {'name': 'Samsung QLED 55', 'price': 79990, 'stock': 3, 'image_url': 'https://example.com/samsungqled55.jpg', 'diaganal': '55'},
        {'name': 'LG OLED 48', 'price': 99990, 'stock': 2, 'image_url': 'https://example.com/lgoled48.jpg', 'diaganal': '48'},
        {'name': 'Sony Bravia 65', 'price': 129990, 'stock': 1, 'image_url': 'https://example.com/sonybravia65.jpg', 'diaganal': '65'},
        {'name': 'Philips Ambilight 50', 'price': 69990, 'stock': 4, 'image_url': 'https://example.com/philips50.jpg', 'diaganal': '50'},
        {'name': 'TCL 43', 'price': 39990, 'stock': 6, 'image_url': 'https://example.com/tcl43.jpg', 'diaganal': '43'},
    ],
    # Планшеты
    [
        {'name': 'iPad Pro 11', 'price': 79990, 'stock': 7, 'image_url': 'https://example.com/ipadpro11.jpg', 'diaganal': '11'},
        {'name': 'Samsung Galaxy Tab S8', 'price': 59990, 'stock': 10, 'image_url': 'https://example.com/galaxytabs8.jpg', 'diaganal': '11'},
        {'name': 'Lenovo Tab P11', 'price': 29990, 'stock': 12, 'image_url': 'https://example.com/lenovop11.jpg', 'diaganal': '11.5'},
        {'name': 'Huawei MatePad 10', 'price': 34990, 'stock': 8, 'image_url': 'https://example.com/matepad10.jpg', 'diaganal': '10.4'},
        {'name': 'Xiaomi Pad 5', 'price': 39990, 'stock': 9, 'image_url': 'https://example.com/xiaomipad5.jpg', 'diaganal': '11'},
    ],
    # Аксессуары
    [
        {'name': 'Apple AirPods Pro', 'price': 24990, 'stock': 20, 'image_url': 'https://example.com/airpodspro.jpg', 'diaganal': '-'},
        {'name': 'Samsung Galaxy Buds2', 'price': 12990, 'stock': 18, 'image_url': 'https://example.com/galaxybuds2.jpg', 'diaganal': '-'},
        {'name': 'Xiaomi Mi Band 7', 'price': 4990, 'stock': 25, 'image_url': 'https://example.com/miband7.jpg', 'diaganal': '-'},
        {'name': 'Baseus Power Bank', 'price': 2990, 'stock': 30, 'image_url': 'https://example.com/baseuspower.jpg', 'diaganal': '-'},
        {'name': 'UGREEN USB-C Cable', 'price': 990, 'stock': 50, 'image_url': 'https://example.com/ugreencable.jpg', 'diaganal': '-'},
    ],
]

for i, cat in enumerate(categories):
    c = Category.objects.create(**cat)
    for prod in products[i]:
        Product.objects.create(category=c, **prod) 