from django.db import models
from users.models import User


class Customer(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    code = models.CharField(max_length=3, unique=True)
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='customers')

    def __str__(self):
        return f"{self.name} ({self.code})"


class Order(models.Model):
    ORDER_TYPE_CHOICES = [
        ('Н', 'Нестандартные заказы не относящиеся к кухням'),
        ('K', 'Нестандартные заказы кухонь'),
        ('ЛК', 'Стандартный заказ на кухни'),
        ('ЭШ', 'Стандартный заказ на Шкафы'),
        ('П', 'Порталы'),
    ]
    STATUS_CHOICES = [
        ('accepted', 'Принят'),
        ('in_progress', 'В работе'),
        ('clarification', 'Уточнение'),
        ('documents', 'Документы'),
        ('postponed', 'Перенос'),
        ('completed', 'Готово'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Заказчик')
    order_number = models.CharField(max_length=20, unique=True)
    order_type = models.CharField(max_length=3, choices=ORDER_TYPE_CHOICES)
    month = models.IntegerField(max_length=10)
    week = models.IntegerField()
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='managed_orders')
    mass = models.FloatField()
    number_of_packages = models.IntegerField()
    processing_start_date = models.DateField()
    technologist = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='processed_orders')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    has_mdf = models.BooleanField()
    has_furniture = models.BooleanField()
    has_glass = models.BooleanField()
    has_cnc = models.BooleanField()
    area_ldsp = models.FloatField()
    area_mdf = models.FloatField()
    edge_0_4mm = models.FloatField()
    edge_2mm = models.FloatField()
    edge_1mm = models.FloatField()
    total_material_area = models.FloatField()
    serial_product_area = models.FloatField()
    fireplace_portal_area = models.FloatField()
    reason_for_claim = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.order_number
