from django.db import models


class Manufacturer(models.Model):  # Производитель
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class CreditApplication(models.Model):  # Кредитная заявка
    created_at = models.DateTimeField(auto_now_add=True)


class Contract(models.Model):  # Контракт
    credit_application = models.OneToOneField(CreditApplication, on_delete=models.CASCADE, related_name='contract')
    created_at = models.DateTimeField(auto_now_add=True)


class Product(models.Model):  # Товар
    name = models.CharField(max_length=255)
    credit_application = models.ForeignKey(CreditApplication, on_delete=models.CASCADE, related_name='products')
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)

