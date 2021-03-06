from django.db import models
from django.contrib.auth.models import AbstractUser
from utils.helpers import validate_phone_number
# Create your models here.


class User(AbstractUser):
    ROLES = (
        ('admin', 'admin'),
        ('regular', 'regular')
    )
    email = models.EmailField(unique=True)
    role = models.CharField(choices=ROLES, max_length=20, default='regular')
    phone_number = models.CharField(max_length=20, unique=True, validators=[validate_phone_number])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']
        db_table = 'user'
