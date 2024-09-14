from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils import timezone
from django.db.models import ProtectedError
import logging
from django.db import transaction
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.contrib.auth import get_user_model


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
    activation_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.username
    
    def activate(self):
        self.is_active = True
        self.activation_date = timezone.now()
        self.save()

    def deactivate(self):
        self.is_active = False
        self.save()


class Membership(models.Model):
    name = models.CharField(max_length=50, default="Membresía Estándar")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=250.00)
    currency = models.CharField(max_length=3, default="MXN")

    def __str__(self):
        return f"{self.name} - {self.price} {self.currency}"
    

User = get_user_model()

class PhotographerAvailability(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.date} - {self.start_time} to {self.end_time}"

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    MEETING_TYPES = (
        ('video', 'Videollamada'),
        ('in_person', 'Reunión presencial'),
    )
    meeting_type = models.CharField(max_length=10, choices=MEETING_TYPES)
    LOCATIONS = (
        ('lugar1', 'Lugar 1'),
        ('lugar2', 'Lugar 2'),
    )
    location = models.CharField(max_length=10, choices=LOCATIONS)
    additional_message = models.TextField(blank=True, null=True)
    PAYMENT_METHODS = (
        ('deposit', 'Depósito bancario'),
        ('cash', 'Efectivo'),
    )
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHODS)
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.date} {self.time}"
    