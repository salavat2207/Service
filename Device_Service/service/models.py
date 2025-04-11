from datetime import date

from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Device(models.Model):
    DEVICE_TYPES = [
        ('apple', 'Apple'),
        ('samsung', 'Samsung'),
        ('xiaomi', 'Xiaomi'),
        ('dyson', 'Dyson'),
        ('vacuum_cleaner', 'Пылесосы'),
        ('console', 'Игровые консоли'),
    ]

    type = models.CharField(max_length=50, choices=DEVICE_TYPES)  #тип модели
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='devices') #бренд
    model_name = models.CharField(max_length=50) #модель
    repair_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) #стоимость ремонта
    repair_status = models.TextField(blank=True, null=True) #статус ремонта
    diagnostics_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0) #диагностика


    def __str__(self):
        return f"{self.get_type_display()} {self.brand.name} {self.model_name}"


"""
Реализация формы обратной связи
"""
class Feedback(models.Model):
    name = models.CharField(max_length=50) #имя
    phone = models.DecimalField(max_digits=10, decimal_places=0) #телефон
    message = models.TextField() #сообщение
    # created_at = models.DateTimeField(auto_now_add=True) #дата создания
    reply = models.TextField(blank=True, null=True) #ответ на сообщение
    replied = models.BooleanField(default=False) #отвечено или нет

    def __str__(self):
        return f"{self.name} ({'отвечено' if self.replied else 'ожидает ответа'})"


