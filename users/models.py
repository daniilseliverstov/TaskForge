from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    DEPARTMENT_CHOICES = [
        ('commercial', 'Коммерческий'),
        ('technical', 'Технический'),
        ('construction', 'Конструкторский'),
        ('supply', 'Снабжение'),
    ]

    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)
