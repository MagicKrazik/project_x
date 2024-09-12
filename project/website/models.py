from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils import timezone
from django.db.models import ProtectedError
import logging
from django.db import transaction
from django.db.models.signals import pre_delete
from django.dispatch import receiver

class CustomUser(AbstractUser):
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('overdue', 'Overdue'),
    ]

    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='pending')
    registration_date = models.DateTimeField(auto_now_add=True)
    last_payment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.username


class Membership(models.Model):
    name = models.CharField(max_length=50, default="Membresía Estándar")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=250.00)
    currency = models.CharField(max_length=3, default="MXN")

    def __str__(self):
        return f"{self.name} - {self.price} {self.currency}"
    