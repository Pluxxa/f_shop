# models.py
from django.db import models

class Product(models.Model):
    TYPE_CHOICES = [
        ('flowers', 'Цветы'),
        ('bouquets', 'Букеты'),
    ]

    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    image = models.ImageField(upload_to='product_images/', blank=True, null=True, verbose_name="Изображение")
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, verbose_name="Тип товара")
    is_active = models.BooleanField(default=True, verbose_name="Активный товар")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок отображения")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name
