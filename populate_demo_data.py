import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop_backend.settings")
django.setup()

from shop.models import Category, Product

categories = [
    {"name": "Смартфоны", "description": "Мобильные телефоны и смартфоны"},
    {"name": "Ноутбуки", "description": "Персональные ноутбуки для работы и учебы"},
    {"name": "Телевизоры", "description": "Современные телевизоры разных диагоналей"},
    {
        "name": "Планшеты",
        "description": "Планшетные компьютеры для развлечений и работы",
    },
    {"name": "Аксессуары", "description": "Чехлы, зарядки, кабели и другие аксессуары"},
]

products = [
    # Смартфоны
    [
        {
            "name": "iPhone 14",
            "price": 79990,
            "stock": 10,
            "image_url": "https://cdn.mediapark.uz/imgs/9f825454-3b70-4df1-a816-4f41e347d288_1.webp",
            "diaganal": "6.1",
        },
        {
            "name": "Samsung Galaxy S23",
            "price": 69990,
            "stock": 15,
            "image_url": "https://castore.uz/upload/iblock/7bb/59q77vbtq4wywzhuaw2920xin488oymh/smartfon-samsung-galaxy-s23-ultra-sm-s918b-ds-512gb-light-pink.jpg",
            "diaganal": "6.1",
        },
        {
            "name": "Xiaomi 13",
            "price": 49990,
            "stock": 20,
            "image_url": "https://mini-io-api.texnomart.uz/catalog/product/3551/355179/187152/4ee159ca-62f3-4def-aaeb-c6367b5df9c6.jpg",
            "diaganal": "6.36",
        },
        {
            "name": "Google Pixel 7",
            "price": 59990,
            "stock": 8,
            "image_url": "https://olcha.uz/image/700x700/products/supplier/stores/1/2023-05-15/iXYSeuF0RrbD8hXrpVGHPfzkbY3NKNWwTSMfPD5p1HBfZqLriPEGt6iCnGGH.jpg",
            "diaganal": "6.3",
        },
        {
            "name": "OnePlus 11",
            "price": 54990,
            "stock": 12,
            "image_url": "https://oasis.opstatics.com/content/dam/oasis/page/2023/na/oneplus-11/specs/green-img.png",
            "diaganal": "6.7",
        },
    ],
    # Ноутбуки
    [
        {
            "name": "MacBook Air M2",
            "price": 119990,
            "stock": 5,
            "image_url": "https://maxcom.uz/storage/product/oRhF3mdkGO70yQJX836mY26GXqBICK0zV5cNVxll.png",
            "diaganal": "13.6",
        },
        {
            "name": "Dell XPS 13",
            "price": 99990,
            "stock": 7,
            "image_url": "https://olcha.uz/image/600x600/products/2022-08-01/noutbuk-dell-xps-13-9310-i7-1165g7-16512gb-ssd-134-87164-0.jpeg",
            "diaganal": "13.4",
        },
        {
            "name": "HP Spectre x360",
            "price": 89990,
            "stock": 6,
            "image_url": "https://maxcom.uz/storage/product/m4QVyLniqSm2j1DNy6otwSfYCpxdz3TSEo3m40SM.jpeg",
            "diaganal": "13.5",
        },
        {
            "name": "Lenovo ThinkPad X1",
            "price": 109990,
            "stock": 4,
            "image_url": "https://www.icd.uz/upload/iblock/dfe/njo3yqps0igjmga1qz6bgb7if1xk3pnb.jpg",
            "diaganal": "14",
        },
        {
            "name": "ASUS ZenBook 14",
            "price": 84990,
            "stock": 9,
            "image_url": "https://assets.asaxiy.uz/product/items/desktop/658486cf70584dd9fe9c9cc48af531052025091615464990451tQAeP5Pzr6.png",
            "diaganal": "14",
        },
    ],
    # Телевизоры
    [
        {
            "name": "Samsung QLED 55",
            "price": 79990,
            "stock": 3,
            "image_url": "https://tezz.uz/uploads/images/product/521/thumbs/211249-10501050.jpg",
            "diaganal": "55",
        },
        {
            "name": "LG OLED 48",
            "price": 99990,
            "stock": 2,
            "image_url": "https://ir.ozone.ru/s3/multimedia-1-t/c1000/7021028513.jpg",
            "diaganal": "48",
        },
        {
            "name": "Sony Bravia 65",
            "price": 129990,
            "stock": 1,
            "image_url": "https://i5.walmartimages.com/asr/78c61234-9ad2-4205-89d2-4b45d6853da0.a6f29b09cbff2b31953f4626cfa5b312.jpeg",
            "diaganal": "65",
        },
        {
            "name": "Philips Ambilight 50",
            "price": 69990,
            "stock": 4,
            "image_url": "https://touch.com.ua/upload/iblock/9e4/rzxuija36egtopsoayd2dfuz25mf6zey.jpg",
            "diaganal": "50",
        },
        {
            "name": "TCL 43",
            "price": 39990,
            "stock": 6,
            "image_url": "https://olcha.uz/image/700x700/products/cdn_1/supplier/stores/1/2025-01-04/cA44x97HbGshzx38N4u8J2XU8VsoXgNqAoUPblXR9AiIqiupQg9ekxxfrQ1I.jpg",
            "diaganal": "43",
        },
    ],
    # Планшеты
    [
        {
            "name": "iPad Pro 11",
            "price": 79990,
            "stock": 7,
            "image_url": "https://toptop.uz/storage/offer/images/planset-apple-ipad-pro-11-2020-512gb-wi-fi-gray-silver_43d6206be22d2f93f3b30067ee2819a12020050220250382800k4Cv9dyVdM.jpg",
            "diaganal": "11",
        },
        {
            "name": "Samsung Galaxy Tab S8",
            "price": 59990,
            "stock": 10,
            "image_url": "https://olcha.uz/image/700x700/products/supplier/stores/1/2023-07-05/7Zd07RsUgJ9NWCvdjhC7EmIVQ6RBgUTUri07jf4Ytn87SwclLcJYXPlk9T0C.jpg",
            "diaganal": "11",
        },
        {
            "name": "Lenovo Tab P11",
            "price": 29990,
            "stock": 12,
            "image_url": "https://manuals.plus/wp-content/uploads/2022/04/Lenovo-Tab-P11-Smart-Tablet-IMAGE.png",
            "diaganal": "11.5",
        },
        {
            "name": "Huawei MatePad 10",
            "price": 34990,
            "stock": 8,
            "image_url": "https://consumer.huawei.com/dam/content/dam/huawei-cbg-site/common/mkt/pdp/admin-image/tablets/matepad-se/specs/specs-img.png",
            "diaganal": "10.4",
        },
        {
            "name": "Xiaomi Pad 5",
            "price": 39990,
            "stock": 9,
            "image_url": "https://olcha.uz/image/700x700/products/2022-11-04/xiaomi-pad-5-166541-0.jpeg",
            "diaganal": "11",
        },
    ],
    # Аксессуары
    [
        {
            "name": "Apple AirPods Pro",
            "price": 24990,
            "stock": 20,
            "image_url": "https://cdn.flymart.uz/file/hub/file/2024/12/26/2qkEDPtAaTiXSzN6mdbBYK2mOhM.jpg",
            "diaganal": "-",
        },
        {
            "name": "Samsung Galaxy Buds2",
            "price": 12990,
            "stock": 18,
            "image_url": "https://castore.uz/upload/iblock/3f3/hneoms9iqrhzbvkxfklcii4wmmd0j5bz/besprovodnye-naushniki-samsung-galaxy-buds-2-sm-r177n-black.jpg",
            "diaganal": "-",
        },
        {
            "name": "Xiaomi Mi Band 7",
            "price": 4990,
            "stock": 25,
            "image_url": "https://i02.appmifile.com/bg_m.jpg",
            "diaganal": "-",
        },
        {
            "name": "Baseus Power Bank",
            "price": 2990,
            "stock": 30,
            "image_url": "https://spphone.uz/wp-content/uploads/2023/04/eng_pl_Baseus-Qpow-powerbank-10000mAh-built-in-USB-Type-C-cable-22-5W-Quick-Charge-SCP-AFC-FCP-black-PPQD020101-95332_3.png",
            "diaganal": "-",
        },
        {
            "name": "UGREEN USB-C Cable",
            "price": 990,
            "stock": 50,
            "image_url": "https://tgrad.kz/upload/resize_cache/iblock/248/1000_1000_1/ysad40uj6zvxipb7o3jekuajcgi9osdq.jpg",
            "diaganal": "-",
        },
    ],
]

for i, cat in enumerate(categories):
    c = Category.objects.create(**cat)
    for prod in products[i]:
        Product.objects.create(category=c, **prod)
