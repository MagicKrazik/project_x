# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils import timezone

class User(AbstractUser):
    nombre = models.CharField(max_length=100, null=True, blank=True)  # Make it nullable for existing users
    telefono = models.CharField(max_length=15, null=True, blank=True)  # Make it nullable for existing users
    metodo_pago = models.CharField(
        max_length=20, 
        choices=[
            ('online', 'Pago en línea'),
            ('deposito', 'Depósito bancario')
        ],
        default='online',
        null=True,
        blank=True
    )
    last_payment_date = models.DateField(null=True, blank=True)
    next_payment_date = models.DateField(null=True, blank=True)

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='custom_user_set',
        related_query_name='custom_user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_set',
        related_query_name='custom_user',
    )

    def save(self, *args, **kwargs):
        if not self.last_payment_date:
            self.last_payment_date = timezone.now().date()
            self.next_payment_date = self.last_payment_date + timezone.timedelta(days=30)
        super().save(*args, **kwargs)

class Membership(models.Model):
    name = models.CharField(max_length=50, default="Membresía Estándar")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=250.00)
    currency = models.CharField(max_length=3, default="MXN")

    def __str__(self):
        return f"{self.name} - {self.price} {self.currency}"